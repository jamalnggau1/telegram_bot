import json

import requests as requests
from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types.callback_query import CallbackQuery

import constants
from constants import host
from data import config
from keyboards.inline.callback_data import checking_meeting, meeting_status_callback
from loader import dp


# @dp.message_handler(Command("chack"))
# async def meetingg(message: types.Message):
#     text = f'🙌 Привет! Уже успел пообщаться с собеседником?'
#
#     a = InlineKeyboardMarkup(
#         row_width=3,
#         inline_keyboard=[
#             [
#                 InlineKeyboardButton(
#                     text='Да, всё гуд',
#                     callback_data=checking_meeting.new(status="ok_good!"),
#
#                 ),
#                 InlineKeyboardButton(
#                     text='Нет, ещё не общались',
#                     callback_data=checking_meeting.new(status="not_communicate")
#
#                 ),
#                 InlineKeyboardButton(
#                     text='Парнёр не отвечает',
#                     callback_data=checking_meeting.new(status="not_answer")
#
#                 )
#             ]
#         ]
#     )
#
#     url = f'https://api.telegram.org/bot{config.BOT_TOKEN}/sendMessage?chat_id={336006405}&text={text}&reply_markup={a}'
#
#     payload = {}
#     headers = {}
#
#     response = requests.request("POST", url, headers=headers, data=payload)



@dp.callback_query_handler(checking_meeting.filter(status="ok_good!"))
async def checking_meeting_ok_good(callback: CallbackQuery):
    await callback.answer(cache_time=10)

    text = f'😎 Отлично! Хочешь найдём ещё одного собеседника?'

    a = InlineKeyboardMarkup(
        row_width=2,
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text='Да',
                    callback_data=meeting_status_callback.new(status="meeting_status = waiting"),

                ),
                InlineKeyboardButton(
                    text='Нет',
                    callback_data=meeting_status_callback.new(status="meeting_status = not ready")

                ),

            ]
        ]
    )

    url = f'https://api.telegram.org/bot{config.BOT_TOKEN}/sendMessage?chat_id={callback.from_user.id}&text={text}&reply_markup={a}'

    payload = {}
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload)


@dp.callback_query_handler(checking_meeting.filter(status="not_communicate"))
async def checking_meeting_not_communicate(callback: CallbackQuery):
    await callback.answer(cache_time=10)

    text = f'Подожди чуть-чуть, мы напомним о встрече собеседнику'

    url = f'https://api.telegram.org/bot{config.BOT_TOKEN}/sendMessage?chat_id={callback.from_user.id}&text={text}'

    payload = {}
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload)


@dp.callback_query_handler(checking_meeting.filter(status="not_answer"))
async def checking_meeting_not_answer(callback: CallbackQuery):
    await callback.answer(cache_time=10)

    text = f'🧙‍♀️ Может тогда поменяем его?'

    a = InlineKeyboardMarkup(
        row_width=2,
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text='Я подожду',
                    callback_data=checking_meeting.new(status="I_wait"),

                ),
                InlineKeyboardButton(
                    text='«Поменять»',
                    callback_data=checking_meeting.new(status="change_partner")

                ),

            ]
        ]
    )

    url = f'https://api.telegram.org/bot{config.BOT_TOKEN}/sendMessage?chat_id={callback.from_user.id}&text={text}&reply_markup={a}'

    payload = {}
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload)


@dp.callback_query_handler(checking_meeting.filter(status="I_wait"))
async def checking_meeting_I_wait(callback: CallbackQuery):
    await callback.answer(cache_time=10)

    text = f'Хорошо, надеемся собеседник ответит.'
    url = f'https://api.telegram.org/bot{config.BOT_TOKEN}/sendMessage?chat_id={callback.from_user.id}&text={text}'

    payload = {}
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload)


@dp.callback_query_handler(checking_meeting.filter(status="change_partner"))
async def checking_meeting_status_change_partner(callback: CallbackQuery):
    await callback.answer(cache_time=10)

    url = host + "/filling_profile/stop_meet_change_partner/"
    print(f'***********{callback.from_user.id}')
    payload = json.dumps({
        "profile_id": {callback.from_user.id},
        "machine_token": {constants.a}
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
