import datetime
from random import randint

from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery

from keyboards.inline.callback_data import registration_callback
from keyboards.inline.inline_buttons import meeting_status_button
from loader import dp, pg_db


@dp.message_handler(Command("meeting"))
async def meeting(message: types.Message):
    await pg_db.create()

    await message.answer('Ты выбрал опцию сформировать встречи')

    all_profiles = await pg_db.select_all_profiles_for_meeting()


    await message.answer('четное число профилей')

    while len(all_profiles) > 0:
        print(f'-------------Весь список до взятия первого: {all_profiles}---------------------')
        first_profile = all_profiles.pop(0)
        print(f'-------------Первый пользователь: {first_profile[1]}---------------------')
        print(f'-------------Весь список после взятия первого: {all_profiles}---------------------')

        selection_list=all_profiles.copy()

        meeting_success=False
        while (len(selection_list) > 0) and (not meeting_success):
            second_profile_number = randint(0, len(selection_list) - 1)
            second_profile = selection_list[second_profile_number]
            print(f'-------------Второй пользователь: {second_profile[1]}-------------------')
            print(f'-------------Весь список после взятия второго: {all_profiles}---------------------')

            # if ..... проверка встречались ли first_profile и second_profile до этого

            meeting_list = await pg_db.select_meet_list(first_profile[1])

            meeting_indicator = False
            for meet in meeting_list:

                if second_profile[1] == meet[6]:
                    meeting_indicator = True
                    print(f'-------------meeting_indicator = True. А весь список при этом: {all_profiles}---------------------')


            if meeting_indicator == False:
                print(f'------------Пара сформирована--------------')
                await pg_db.add_meet(first_profile[1], second_profile[1], date_meeting=datetime.datetime.now())
                meeting_success=True
            else:
                selection_list.pop(second_profile_number)
                print(f'------------Такая пара уже была--------------')
                print(f'-------------А весь список при этом: {all_profiles}---------------------')

        if meeting_success == True:
            print(f'-------------Удаляем пользователя: {all_profiles[second_profile_number]}---------------------')
            all_profiles.pop(second_profile_number)







@dp.callback_query_handler(registration_callback.filter(status="change_meeting_status"))
async def change_meeting_status(callback: CallbackQuery):
    await callback.answer(cache_time=10)

    await pg_db.create()

    full_name = callback.from_user.full_name
    profile = await pg_db.select_profile(contacts=full_name)
    current_meeting_status = profile[7]

    if current_meeting_status == "meeting":
        text_message = (f"Твой текущий статус: {current_meeting_status}. Это означает, что пара тебе подобрана, "
                        f"и встреча сейчас в самом разгаре. ")
    elif current_meeting_status == "waiting":
        text_message = (f"Твой текущий статус: {current_meeting_status}. Это означает, что мы пытаемся "
                        f"подобрать для тебя подходящую пару. ")
    elif current_meeting_status == "not ready":
        text_message = (f"Твой текущий статус: {current_meeting_status}. Это означает, что ты не готов "
                        f"к встречам на этой неделе. ")

    await callback.message.answer(text_message + "Измени статус на:",
                                  reply_markup=meeting_status_button("waiting", "not ready"))


@dp.callback_query_handler(registration_callback.filter(status="meeting_status = waiting"))
async def meeting_status_waiting(callback: CallbackQuery):
    await callback.answer(cache_time=10)

    await pg_db.create()
    full_name = callback.from_user.full_name

    await pg_db.update_profile_meeting_status("waiting", full_name)

    profile = await pg_db.select_profile(contacts=full_name)
    current_meeting_status = profile[7]
    await callback.message.answer(f"Статус  изменен на: {current_meeting_status}")

    profile_for_meeting = await pg_db.select_profile_for_meeting(profile[2])

    if profile_for_meeting is None:
        await pg_db.add_profile_for_meetting(profile[2])
        await callback.message.answer(f"Вы добавлены в таблицу поиска")

    else:
        await callback.message.answer(f"Вы уже есть в таблице для поиска")


@dp.callback_query_handler(registration_callback.filter(status="meeting_status = not ready"))
async def meeting_status_not_ready(callback: CallbackQuery):
    await callback.answer(cache_time=10)

    await pg_db.create()
    full_name = callback.from_user.full_name

    await pg_db.update_profile_meeting_status("not ready", full_name)

    profile = await pg_db.select_profile(contacts=full_name)
    current_meeting_status = profile[7]
    await callback.message.answer(f"Статус  изменен на: {current_meeting_status}")

    profile_for_meeting = await pg_db.select_profile_for_meeting(profile[2])

    if profile_for_meeting is not None:
        await pg_db.delete_profile_for_meeting(profile[2])
        await callback.message.answer(f"Вы убраны из таблицы поиска")
    else:
        await callback.message.answer(f"Вас не было в таблице поиска")
