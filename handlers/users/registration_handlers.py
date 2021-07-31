import datetime
from random import random, randrange, getrandbits, randint

import requests
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from data import config
from keyboards.inline.callback_data import registration_callback
from loader import dp, users_db, pg_db
from states import Registration_states


@dp.callback_query_handler(registration_callback.filter(status="reg"))
async def reg_bot(callback: CallbackQuery):
    await callback.answer(cache_time=10)

    await callback.message.answer(f"Начнем с электронной почты ⬇")

    await Registration_states.enter_email.set()


@dp.message_handler(state=Registration_states.enter_email)
async def enter_email(message: types.Message, state: FSMContext):
    email = message.text
    full_name = message.from_user.full_name
    user_name = "@"+message.from_user.username

    await pg_db.add_profile(full_name, email, contacts=user_name)

    await message.answer(f"Ты зарегестрирован.")

    a = requests.post('http://' + config.IP + ':' + config.PORT + '/filling_profile/',
                      params={'full_name': message.from_user.full_name,
                              'email': email,
                              'contacts': user_name
                              })

    await message.answer(f"Я записал тебя. Если хочешь дополнить информацию, можешь перейти по ссылке {a.url}")
    await state.finish()
