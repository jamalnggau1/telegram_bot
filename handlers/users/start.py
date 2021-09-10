
import requests as requests
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command, CommandStart

from constants import host

import constants

from data import config
from text_constants import change_profile, change_meeting_status
from keyboards.inline.callback_data import change_meeting_status_callback
from keyboards.inline.inline_buttons import one_button, change_profile_or_status_button
from loader import dp
from request_to_server.requests import login
from states import Registration_states


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

        await message.answer(text, reply_markup=change_profile_or_status_button(change_profile,
                                                                                requests.post(url,
                                                                                    params={'token': login(user_id,
                                                                                                           constants.a).json().get(
                                                                                        "token"),
                                                                                            'contacts': user_id}).url,
                                                                                change_meeting_status)
                             )

    # profile не найден
    else:
        await message.answer(
            f'Привет 👋. На связи {bot_username}, позволь рассказать немного о себе Каждую неделю я  буду искать тебе '
            f"случайного собеседника, чтобы вместе делать интересные вещи: изучать язык, обсуждать кейсы, найти что-то "
            f"свое или просто развлечься вечером. Теперь пойдем за мной, я расскажу, что делать, чтобы скорее найти собеседника🧙‍♂")

        await message.answer(f"Первым делом, напиши свою почту для регистрации⏬")

        await Registration_states.enter_email.set()










