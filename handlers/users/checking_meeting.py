
from aiogram.types.callback_query import CallbackQuery
import requests as requests
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart, Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.json import json
from keyboards.inline.callback_data import change_meeting_status_callback, edite_profile_callback

from constants import host

import schedule, time

import constants

from data import config
from keyboards.inline.callback_data import checking_meeting
from loader import skills_categories_db, pg_db

from keyboards.inline.inline_buttons import regestration_button, change_profile_or_status_button
from loader import dp, users_db
from request_to_server.requests import login





@dp.message_handler(Command("chack"))
async def meetingg(message: types.Message):

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





        @dp.callback_query_handler(checking_meeting.filter(status="not_communicate"))
        async def checking_meeting_not_communicate(callback: CallbackQuery):

            await callback.answer(cache_time=10)

            text = f'Подожди чуть-чуть, мы напомним о встрече собеседнику'

            url = f'https://api.telegram.org/bot{config.BOT_TOKEN}/sendMessage?chat_id={336006405}&text={text}'


            payload={}
            headers = {}

            response = requests.request("POST", url, headers=headers, data=payload)





        @dp.callback_query_handler(checking_meeting.filter(status="not_answer"))
        async def checking_meeting_not_answer(callback: CallbackQuery):


            await callback.answer(cache_time=10)




            text = f'🧙‍♀️ Может тогда поменяем его?'

            a= InlineKeyboardMarkup(
                row_width=2,
                inline_keyboard=[
                    [
                        InlineKeyboardButton(
                            text='Я подожду',
                            callback_data=checking_meeting.new(status="ok,_good!"),

                        ),
                        InlineKeyboardButton(
                            text='«Поменять»',
                            callback_data=checking_meeting.new(status="not_communicate")

                        ),
                    
                    ]
                ]
            )


            url = f'https://api.telegram.org/bot{config.BOT_TOKEN}/sendMessage?chat_id={336006405}&text={text}&reply_markup={a}'


            payload={}
            headers = {}

            response = requests.request("POST", url, headers=headers, data=payload)