
import constants
from keyboards.inline.inline_buttons import one_button
from request_to_server.requests import login
from data import config
import json

import requests
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from keyboards.inline.callback_data import change_meeting_status_callback
from loader import dp
from states import Registration_states
from constants import host


@dp.callback_query_handler(change_meeting_status_callback.filter(status="reg"))
async def reg_bot(callback: CallbackQuery):
    await callback.answer(cache_time=10)

    await callback.message.answer(f"Первым делом, напиши свою почту для регистрации⏬")

    await Registration_states.enter_email.set()


@dp.message_handler(state=Registration_states.enter_email)
async def enter_email(message: types.Message, state: FSMContext):
    email = message.text
    full_name = message.from_user.full_name
    # user_name = "@" + message.from_user.username
    user_id = message.from_user.id

    # await pg_db.add_profile(full_name, email, contacts=user_name)

    url =host+ "/filling_profile/users/"

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

        text = f'Теперь поделись своими интересами. Таким образом вы сможете лучше узнать друг о друге еще до встречи. Совпадающие интересы помогут быстро найти общие темы для общения. Но и различные интересы  часто дарят  множество  открытий для собеседников. Не волнуйся, ты всегда можешь изменить данные в своем профиле с помощью команды /profile'
        url = host + f'''/filling_profile/'''

        await message.answer(text, reply_markup=one_button(text_btn="Заполнить профиль",url=requests.post(url, params={'token': login(user_id, constants.a).json().get("token"),'contacts': user_id}).url))
        await state.finish()

    else:
        await message.answer(f"Аккаунт не был зарегистрирован. Ошибка сервера при заполнении почты")

