import requests
from aiogram import types
from aiogram.dispatcher import FSMContext

import constants
from constants import host, api_constant
from enum_constans import share_your_interests, if_you_have_questions_use_help, invalid_email
from keyboards.inline.inline_buttons import one_button
from loader import dp
from request_to_server.requests import login, registration
from states import Registration_states
from utils.validation import is_valid_email


@dp.message_handler(state=Registration_states.enter_email)
async def enter_email(message: types.Message, state: FSMContext):
    email = message.text
    print(f'email: {email}')
    full_name = message.from_user.full_name
    user_id = message.from_user.id


    if not is_valid_email(email):
        await message.answer(invalid_email)
        return
    else:


        registration_response = registration(user_id, full_name, email)
        if registration_response.status_code == 201:

            text = share_your_interests
            url = host + '/filling_profile/'
            await message.answer(text, reply_markup=one_button(text_btn="Заполнить профиль", url=requests.post(url, params={
                'token': login(user_id, constants.machine_token_constant).json().get("token"), 'contacts': user_id}).url))
            await state.finish()

        else:
            await message.answer(f"Аккаунт не был зарегистрирован. Ошибка сервера при заполнении почты")
            await state.finish()
