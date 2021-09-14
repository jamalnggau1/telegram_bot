import requests
from aiogram import types
from aiogram.dispatcher import FSMContext

import constants
from constants import host
from enum_constans import share_your_interests
from keyboards.inline.inline_buttons import one_button
from loader import dp
from request_to_server.requests import login, registration
from states import Registration_states


@dp.message_handler(state=Registration_states.enter_email)
async def enter_email(message: types.Message, state: FSMContext):
    email = message.text
    full_name = message.from_user.full_name
    user_id = message.from_user.id

    registration_response = registration(user_id, full_name, email)

    if registration_response == 201:

        text = share_your_interests
        url = host + f'''/filling_profile/'''

        await message.answer(text, reply_markup=one_button(text_btn="Заполнить профиль", url=requests.post(url, params={
            'token': login(user_id, constants.a).json().get("token"), 'contacts': user_id}).url))
        await state.finish()

    else:
        await message.answer(f"Аккаунт не был зарегистрирован. Ошибка сервера при заполнении почты")
