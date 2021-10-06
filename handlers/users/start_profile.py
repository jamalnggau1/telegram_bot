import requests as requests
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher.filters.builtin import Command
from constants import host, api_constant, machine_token_constant
from data import config
from enum_constans import meeting_status_constant, waiting_status_constant, not_ready_status_constant, write_your_email, \
    blank_profile
from keyboards.inline.callback_data import edite_profile_callback
from keyboards.inline.inline_buttons import one_button, change_profile_or_status_button
from loader import dp
from request_to_server.requests import login
from states import Registration_states
from enum_constans import change_profile, change_meeting_status


@dp.message_handler(CommandStart() | Command("profile"))
async def bot_start(message: types.Message, state: FSMContext):
    # подбираем user_id
    user_id = message.from_user.id

    # определяем username бота
    url = "https://api.telegram.org/bot" + f"{config.BOT_TOKEN}" + "/getMe"
    payload = {}
    headers = {}
    bot_username = "@" + requests.request("POST", url, headers=headers, data=payload).json().get("result").get(
        "username")

    # Если login вернул статус не 200(нет пользователя в базе), предлагаем пользователю зарегаться.
    # status = 200 - Все хорошо profile есть
    request_from_login = login(user_id, machine_token_constant)
    # Если login вернул статус не 200(нет пользователя в базе), предлагаем пользователю зарегаться.
    # status = 200 - Все хорошо profile есть
    if request_from_login.status_code == 200:

        # ссылка для изменения профиля.
        url = host + '/filling_profile/'
        if len(request_from_login.json().get("skills")) >0:
            text = '🪞Карточка профиля🪞\n'
            text += f'''\nСтатус: '''
            # meeting_status из json приходит как str
            meeting_status = int(request_from_login.json().get("meeting_status"))
            if meeting_status == waiting_status_constant:
                text += f'''в поисках собеседника'''
            elif meeting_status == not_ready_status_constant:
                text += f'''не ищу собеседника'''
            elif meeting_status == meeting_status_constant:
                if request_from_login.json().get("companion") is not None:
                    # text += f'''общаюсь с @{request_from_login.json().get("companion")}'''
                    text += 'получил '+f"""<a href="tg://user?id={request_from_login.json().get("companion")}">собеседника☕</a>"""

                else:
                    text += f'''возникла ошибка при выводи статуса поиска встреч. Твой статус: "получил ...", но партнер отсутсвует. Обратись с этой ошибкой в поддержку через /help'''
            else:
                text += f'''возникла ошибка со статусами поиска всреч. Обратись с этой ошибкой в поддержку через /help'''

            text += f'''\nИнтересы: {request_from_login.json().get("skills")}'''
            text += f'''\nМоя почта: {request_from_login.json().get("email")}'''

            print(f'''***********skills:{request_from_login.json().get("skills")}''')
            text += "\nЧто-нибудь изменилось?"

            # Если статус пользователя "meetting", то отправляем сообщение пользователю только с одной кнопкой "изменить профиль".
            if meeting_status == meeting_status_constant:

                await message.answer(text, reply_markup=one_button(text_btn=change_profile,
                                                                   callback_data=edite_profile_callback.new(
                                                                       status="edite_profile"),
                                                                   url=requests.post(url, params={
                                                                       'token': request_from_login.json().get("token"),
                                                                       'contacts': user_id}).url))
            else:
                await message.answer(text, reply_markup=change_profile_or_status_button(change_profile,
                                                                                        requests.post(url, params={
                                                                                            'token': request_from_login.json().get(
                                                                                                "token"),
                                                                                            'contacts': user_id}).url,
                                                                                        change_meeting_status))

        # в profile не заполнены skills
        else:
            await message.answer(blank_profile, reply_markup=one_button(text_btn=change_profile,
                                                               callback_data=edite_profile_callback.new(
                                                                   status="edite_profile"),
                                                               url=requests.post(url, params={
                                                                   'token': request_from_login.json().get("token"),
                                                                   'contacts': user_id}).url))

    # profile не найден
    else:
        await message.answer(f"""Привет 👋. На связи {bot_username}, позволь мне рассказать немного о себе.

📆Каждую неделю я  буду искать тебе случайного собеседника, чтобы вместе делать интересные вещи: изучать язык, обсуждать кейсы, найти что-то свое или просто развлечься вечером.

Теперь попробуем приступить к поиску собеседника🧙‍♂""")

        await message.answer(write_your_email)

        await Registration_states.enter_email.set()
