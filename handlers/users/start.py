import sqlite3

import requests as requests
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart, Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.json import json


from constants import host

import constants

from data import config
from keyboards.inline.callback_data import edite_profile_callback, change_meeting_status_callback
from loader import skills_categories_db, pg_db

from keyboards.inline.inline_buttons import regestration_button, change_profile_or_status_button
from loader import dp, users_db
from request_to_server.requests import login


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message, state: FSMContext):
    # await pg_db.create()

    # подбираем user_id
    user_id = message.from_user.id

    # user_name = "@" + message.from_user.username
    # user = await pg_db.select_profile(contacts=user_name)





    # Если в response статус не 200(нет пользователя в базе), предлагаем пользователю зарегаться.
    # Если пользователь в базе есть, сообщения с кнопками в который вшит топен пользователю отправит сервер через АПИ телеграмма

    # if user is not None:

    print(f'-----------{login(user_id, constants.a).text}')

    # status = 200 - Все хорошо profile есть
    if login(user_id, constants.a).status_code == 200:

        url = host+f'''/filling_profile/'''
        text =f'''Привет 👋 {message.from_user.full_name}! На связи @AndrushaTestbot. Я смотрю ты тут уже не в первый раз. Я о тебе кое-что знаю: '''
        text+=f'''\nEmail📧: {login(user_id, constants.a).json().get("email")}'''
        text+=f'''\nСтатус поиска собеседника: {login(user_id, constants.a).json().get("meeting_status")}'''
        
        if login(user_id, constants.a).json().get("companion") is not None:
            text+=f'''\nУ тебя уже есть стреча. Твой собеседник: @{login(user_id, constants.a).json().get("companion")}'''
        text+="\nЧто желаешь?"

        await message.answer(text, reply_markup=change_profile_or_status_button("изменить профиль",
                                                                          requests.post(
                                                                              url,
                                                                              params={'token': login(user_id, constants.a).json().get("token"), 'contacts':user_id}).url,
                                                                          "изменить статус поиска встречи")
            )

    # profile не найден
    else:
        await message.answer(
            f"Привет 👋 {message.from_user.full_name}! На связи @AndrushaTestbot, я смотрю ты здесь первый раз. Нам "
            f"нужно пройти  регистрацию️", reply_markup=regestration_button)
