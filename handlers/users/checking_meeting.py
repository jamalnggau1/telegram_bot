
import types
from aiogram.dispatcher.filters import Command
from handlers.users.meeting import meeting_status_waiting
from aiogram.types.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup
import requests
from data import config
from keyboards.inline.callback_data import change_meeting_status_callback, edite_profile_callback
from loader import dp
from keyboards.inline.callback_data import checking_meeting
from aiogram.types.callback_query import CallbackQuery
from keyboards.inline.callback_data import change_meeting_status_callback






async def meeting(message: types.Message):

    text = f'🙌 Привет! Уже успел пообщаться с собеседником?'

    a= InlineKeyboardMarkup(
        row_width=3,
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text='Да, всё гуд',
                    callback_data=checking_meeting.new(status="ok_good!"),

                ),
                InlineKeyboardButton(
                    text='Нет, ещё не общались',
                    callback_data=checking_meeting.new(status="not_communicate")

                ),
                InlineKeyboardButton(
                    text='Парнёр не отвечает',
                    callback_data=checking_meeting.new(status="not_answer")

                )
            ]
        ]
    )

    url = f'https://api.telegram.org/bot{config.BOT_TOKEN}/sendMessage?chat_id={336006405}&text={text}&reply_markup={a}'


    payload={}
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload)












    @dp.callback_query_handler(checking_meeting.filter(status="ok_good!"))
    async def checking_meeting_ok_good(callback: CallbackQuery):


        await callback.answer(cache_time=10)

        print(f'***************AAAAAAAAA**********************')



        text = f'😎 Отлично! Хочешь найдём ещё одного собеседника?'

        a= InlineKeyboardMarkup(
            row_width=2,
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text='Да',
                        callback_data=checking_meeting.new(status="ok,_good!"),

                    ),
                    InlineKeyboardButton(
                        text='Нет',
                        callback_data=checking_meeting.new(status="not_communicate")

                    ),
                
                ]
            ]
        )


        url = f'https://api.telegram.org/bot{config.BOT_TOKEN}/sendMessage?chat_id={336006405}&text={text}&reply_markup={a}'


        payload={}
        headers = {}

        response = requests.request("POST", url, headers=headers, data=payload)