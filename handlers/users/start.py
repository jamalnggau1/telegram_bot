import sqlite3

import requests as requests
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart, Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.json import json

import constants
from data import config
from keyboards.inline.callback_data import edite_profile_callback, registration_callback
from loader import skills_categories_db, pg_db

from keyboards.inline.inline_buttons import regestration_button, change_profile_or_status_button
from loader import dp, users_db


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message, state: FSMContext):
    await pg_db.create()

    # подбираем user_id
    user_id = message.from_user.id

    user_name = "@" + message.from_user.username
    user = await pg_db.select_profile(contacts=user_name)

    # формируем POST запрос для проверки есть ли profile с этим user_id
    url = "http://127.0.0.1:8000/filling_profile/users/login/"

    payload = json.dumps({
        "profile": {
            "contacts": user_id,
            "machine_token":constants.a
        }
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(f'--------handler.users.start response.status_code:{response.status_code}---------------')
    print(f'--------handler.users.start response.text:{response.text}---------------')

    meeting_status=response.json().get("meeting_status")

    # Если в response статус не 200(нет пользователя в базе), предлагаем пользователю зарегаться.
    # Если пользователь в базе есть, сообщения с кнопками в который вшит топен пользователю отправит сервер через АПИ телеграмма

    # if user is not None:

    # status = 200 - Все хорошо profile есть
    if response.status_code == 200:

        await message.answer(
            f"Привет 👋 {message.from_user.full_name}! На связи @AndrushaTestbot. Я смотрю ты тут уже не в первый раз. "
            f"Что желаешь?", reply_markup=change_profile_or_status_button("изменить профиль",
                                                                          requests.post(
                                                                              'http://' + config.IP + ':' + config.PORT + '/filling_profile/',
                                                                              params={'contacts': user_name}).url,
                                                                          "изменить статус поиска встречи",meeting_status)
            )

    # profile не найден
    else:
        await message.answer(
            f"Привет 👋 {message.from_user.full_name}! На связи @AndrushaTestbot, я смотрю ты здесь первый раз. Нам "
            f"нужно пройти  регистрацию️", reply_markup=regestration_button)
