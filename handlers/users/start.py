import sqlite3

import requests as requests
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart, Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_data import edite_profile_callback, registration_callback
from loader import skills_categories_db, pg_db

from keyboards.inline.inline_buttons import regestration_button, change_profile_or_status_button
from loader import dp, users_db


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message, state: FSMContext):
    await pg_db.create()
    full_name = message.from_user.full_name
    user = await pg_db.select_profile(full_name=full_name)


    if user is not None:

        await message.answer(f"Привет 👋 {full_name}! На связи @AndrushaTestbot. Я смотрю ты тут уже не в первый раз. "
                             f"Что желаешь?", reply_markup=change_profile_or_status_button("изменить профиль",
                              requests.post('http://127.0.0.1:8000/filling_profile/',
                                           params={'full_name': message.from_user.full_name}).url)
       )
    else:
        await message.answer(f"Привет 👋 {full_name}! На связи @AndrushaTestbot, я смотрю ты здесь первый раз. Нам "
                             f"нужно пройти  регистрацию️ ", reply_markup=regestration_button)


