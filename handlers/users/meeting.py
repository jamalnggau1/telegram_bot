from aiogram.types import CallbackQuery

import constants
from enum_constans import meeting_status_constant, waiting_status_constant, not_ready_status_constant, see_you_in_week, \
    find_companion_on_Monday, error_contact_support
from keyboards.inline.callback_data import change_meeting_status_callback, meeting_status_callback
from loader import dp
from request_to_server.requests import patch, login


# @dp.message_handler(Command("meeting"))
# async def meeting(message: types.Message):
#
#     await message.answer('Ты выбрал опцию сформировать встречи')
#
#     all_profiles = await pg_db.select_all_profiles_for_meeting()
#
#
#     await message.answer('четное число профилей')
#
#     while len(all_profiles) > 0:
#         print(f'-------------Весь список до взятия первого: {all_profiles}---------------------')
#         first_profile = all_profiles.pop(0)
#         print(f'-------------Первый пользователь: {first_profile[1]}---------------------')
#         print(f'-------------Весь список после взятия первого: {all_profiles}----------------------')
#
#         selection_list=all_profiles.copy()
#
#         meeting_success=False
#         while (len(selection_list) > 0) and (not meeting_success):
#             second_profile_number = randint(0, len(selection_list) - 1)
#             second_profile = selection_list[second_profile_number]
#             print(f'-------------Второй пользователь: {second_profile[1]}-------------------')
#             print(f'-------------Весь список после взятия второго: {all_profiles}---------------------')
#
#             # if ..... проверка встречались ли first_profile и second_profile до этого
#
#             meeting_list = await pg_db.select_meet_list(first_profile[1])
#
#             meeting_indicator = False
#             for meet in meeting_list:
#
#                 if second_profile[1] == meet[6]:
#                     meeting_indicator = True
#                     print(f'-------------meeting_indicator = True. А весь список при этом: {all_profiles}---------------------')
#
#
#             if meeting_indicator == False:
#                 print(f'------------Пара сформирована--------------')
#                 await pg_db.add_meet(first_profile[1], second_profile[1], date_meeting=datetime.datetime.now())
#                 meeting_success=True
#             else:
#                 selection_list.pop(second_profile_number)
#                 print(f'------------Такая пара уже была--------------')
#                 print(f'-------------А весь список при этом: {all_profiles}---------------------')
#
#         if meeting_success == True:
#             print(f'-------------Удаляем пользователя: {all_profiles[second_profile_number]}---------------------')
#             all_profiles.pop(second_profile_number)


@dp.callback_query_handler(change_meeting_status_callback.filter(status="change_meeting_status"))
async def change_meeting_status(callback: CallbackQuery):
    await callback.answer(cache_time=10)

    current_meeting_status = login(callback.from_user.id, constants.machine_token_constant).json().get("meeting_status")
    token = login(callback.from_user.id, constants.machine_token_constant).json().get("token")

    if current_meeting_status == waiting_status_constant:
        await callback.message.answer("""Тогда, надеюсь, увидимся в воскресенье, когда мы начинаем неделю новых встреч📬""")
        patch(not_ready_status_constant, token)


    elif current_meeting_status == not_ready_status_constant:
        await callback.message.answer("""Тогда мы начнем поиск немедля. Скоро вернемся с новым собеседником⏰""")
        patch(waiting_status_constant, token)



# Используется в воскресенье, когда нужно в любом случае поставить статус waiting
@dp.callback_query_handler(meeting_status_callback.filter(status="meeting_status = waiting"))
async def meeting_status_waiting(callback: CallbackQuery):
    await callback.answer(cache_time=10)

    token = login(callback.from_user.id, constants.machine_token_constant).json().get("token")

    if patch(waiting_status_constant, token) == 200:
        await callback.message.answer(find_companion_on_Monday)

    else:
        await callback.message.answer(error_contact_support)


# Используется в воскресенье, когда нужно в любом случае поставить статус not ready
@dp.callback_query_handler(meeting_status_callback.filter(status="meeting_status = not ready"))
async def meeting_status_not_ready(callback: CallbackQuery):
    await callback.answer(cache_time=10)

    token = login(callback.from_user.id, constants.machine_token_constant).json().get("token")

    if patch(not_ready_status_constant, token) == 200:
        await callback.message.answer(see_you_in_week)

    else:
        await callback.message.answer(error_contact_support)
