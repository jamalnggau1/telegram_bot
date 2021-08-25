from aiogram.types.callback_query import CallbackQuery
import requests as requests
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart, Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.json import json
from keyboards.inline.callback_data import change_meeting_status_callback, edite_profile_callback,meeting_status_callback

from constants import host

import constants

from data import config
from keyboards.inline.callback_data import checking_meeting
from loader import skills_categories_db, pg_db

from keyboards.inline.inline_buttons import regestration_button, change_profile_or_status_button
from loader import dp, users_db
from request_to_server.requests import login


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message, state: FSMContext):
    # подбираем user_id
    user_id = message.from_user.id

    # определяем username бота
    url = "https://api.telegram.org/bot" + f'{config.BOT_TOKEN}' + "/getMe"
    payload = {}
    headers = {}
    bot_username = "@" + requests.request("POST", url, headers=headers, data=payload).json().get("result").get(
        "username")

    # Если login вернул статус не 200(нет пользователя в базе), предлагаем пользователю зарегаться.
    # status = 200 - Все хорошо profile есть
    if login(user_id, constants.a).status_code == 200:

        url = host + f'''/filling_profile/'''
        text = f'''Привет 👋 {message.from_user.full_name}! На связи {bot_username}. Я смотрю ты тут уже не в первый раз. Я о тебе кое-что знаю: '''
        text += f'''\nEmail📧: {login(user_id, constants.a).json().get("email")}'''
        text += f'''\nСтатус поиска собеседника: {login(user_id, constants.a).json().get("meeting_status")}'''

        if login(user_id, constants.a).json().get("companion") is not None:
            text += f'''\nУ тебя уже есть стреча. Твой собеседник: @{login(user_id, constants.a).json().get("companion")}'''

        print(f'''***********skills:{login(user_id, constants.a).json().get("skills")}''')
        if login(user_id, constants.a).json().get("skills") is not None:
            text += f'''\nТебя интересует: {login(user_id, constants.a).json().get("skills")}'''
        text += "\nЧто желаешь?"

        await message.answer(text, reply_markup=change_profile_or_status_button("изменить профиль",
                                                                                requests.post(
                                                                                    url,
                                                                                    params={'token': login(user_id,
                                                                                                           constants.a).json().get(
                                                                                        "token"),
                                                                                            'contacts': user_id}).url,
                                                                                "изменить статус поиска встречи")
                             )

    # profile не найден
    else:
        await message.answer(
            f"Привет 👋 {message.from_user.full_name}! На связи {bot_username}, я смотрю ты здесь первый раз. Нам "
            f"нужно пройти  регистрацию️", reply_markup=regestration_button)


# def send_messange():
#     # ваша функция отправки сообщений

#     print("Отправка завершена!")

# schedule.every().day.at("15:26").do(send_messange)

# while True: # этот цикл отсчитывает время. Он обязателен.
#     schedule.run_pending()
#     time.sleep(1)









@dp.message_handler(Command("chack"))
async def meetingg(message: types.Message):
    text = f'🙌 Привет! Уже успел пообщаться с собеседником?'

    a = InlineKeyboardMarkup(
        row_width=3,
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text='Да, всё гуд',
                    callback_data=checking_meeting.new(status="ok_good!"),

                ),
                InlineKeyboardButton(
                    text='Нет, ещё не общались',
                    callback_data=checking_meeting.new(status="not_communicate")

                ),
                InlineKeyboardButton(
                    text='Парнёр не отвечает',
                    callback_data=checking_meeting.new(status="not_answer")

                )
            ]
        ]
    )

    url = f'https://api.telegram.org/bot{config.BOT_TOKEN}/sendMessage?chat_id={336006405}&text={text}&reply_markup={a}'

    payload = {}
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload)

    @dp.callback_query_handler(checking_meeting.filter(status="ok_good!"))
    async def checking_meeting_ok_good(callback: CallbackQuery):
        await callback.answer(cache_time=10)

        text = f'😎 Отлично! Хочешь найдём ещё одного собеседника?'

        a = InlineKeyboardMarkup(
            row_width=2,
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text='Да',
                        callback_data=meeting_status_callback.new(status="meeting_status = waiting"),

                    ),
                    InlineKeyboardButton(
                        text='Нет',
                        callback_data=meeting_status_callback.new(status="meeting_status = not ready")

                    ),

                ]
            ]
        )

        url = f'https://api.telegram.org/bot{config.BOT_TOKEN}/sendMessage?chat_id={336006405}&text={text}&reply_markup={a}'

        payload = {}
        headers = {}

        response = requests.request("POST", url, headers=headers, data=payload)

        @dp.callback_query_handler(checking_meeting.filter(status="not_communicate"))
        async def checking_meeting_not_communicate(callback: CallbackQuery):
            await callback.answer(cache_time=10)

            text = f'Подожди чуть-чуть, мы напомним о встрече собеседнику'

            url = f'https://api.telegram.org/bot{config.BOT_TOKEN}/sendMessage?chat_id={336006405}&text={text}'

            payload = {}
            headers = {}

            response = requests.request("POST", url, headers=headers, data=payload)

        @dp.callback_query_handler(checking_meeting.filter(status="not_answer"))
        async def checking_meeting_not_answer(callback: CallbackQuery):
            await callback.answer(cache_time=10)

            text = f'🧙‍♀️ Может тогда поменяем его?'

            a = InlineKeyboardMarkup(
                row_width=2,
                inline_keyboard=[
                    [
                        InlineKeyboardButton(
                            text='Я подожду',
                            callback_data=checking_meeting.new(status="I_wait"),

                        ),
                        InlineKeyboardButton(
                            text='«Поменять»',
                            callback_data=checking_meeting.new(status="change_partner")

                        ),

                    ]
                ]
            )

            url = f'https://api.telegram.org/bot{config.BOT_TOKEN}/sendMessage?chat_id={336006405}&text={text}&reply_markup={a}'

            payload = {}
            headers = {}

            response = requests.request("POST", url, headers=headers, data=payload)






        @dp.callback_query_handler(checking_meeting.filter(status="I_wait"))
        async def checking_meeting_I_wait(callback: CallbackQuery):
            await callback.answer(cache_time=10)

            text = f'Хорошо, надеемся собеседник ответит.'
            url = f'https://api.telegram.org/bot{config.BOT_TOKEN}/sendMessage?chat_id={336006405}&text={text}'

            payload = {}
            headers = {}

            response = requests.request("POST", url, headers=headers, data=payload)



        @dp.callback_query_handler(checking_meeting.filter(status="change_partner"))
        async def checking_meeting_status_change_partner(callback: CallbackQuery):
            await callback.answer(cache_time=10)

            