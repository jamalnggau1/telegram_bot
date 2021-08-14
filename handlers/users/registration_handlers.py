
from data import config
import json

import requests
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from keyboards.inline.callback_data import change_meeting_status_callback
from loader import dp, users_db, pg_db
from states import Registration_states


@dp.callback_query_handler(change_meeting_status_callback.filter(status="reg"))
async def reg_bot(callback: CallbackQuery):
    await callback.answer(cache_time=10)

    await callback.message.answer(f"Начнем с электронной почты ⬇")

    await Registration_states.enter_email.set()


@dp.message_handler(state=Registration_states.enter_email)
async def enter_email(message: types.Message, state: FSMContext):
    email = message.text
    full_name = message.from_user.full_name
    # user_name = "@" + message.from_user.username
    user_id = message.from_user.id

    # await pg_db.add_profile(full_name, email, contacts=user_name)

    url = "http://127.0.0.1:8000/filling_profile/users/"

    payload = json.dumps({
        "profile": {
            "contacts": user_id,
            "full_name": full_name,
            "email": email
        }
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    if response.status_code == 201:
        await message.answer(f"Ты зарегестрирован.")

        a = requests.post('http://' + config.IP + ':' + config.PORT + '/filling_profile/',
                          params={'full_name': message.from_user.full_name,
                                  'email': email,
                                  'contacts': user_id
                                  })

        await message.answer(f"Я записал тебя. Если хочешь дополнить информацию, можешь перейти по ссылке {a.url}")
        await state.finish()

    else:
        await message.answer(f"акк не был записан")
