import json

import requests as requests
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types.callback_query import CallbackQuery

import constants
from constants import host, machine_token_constant
from data import config
from keyboards.inline.callback_data import checking_meeting, meeting_feedback, change_meeting_status_callback
from keyboards.inline.inline_buttons import leave_feedback_buttons, two_buttons
from loader import dp
from request_to_server.requests import getfeedbackfromuser, stop_meet_change_partner


@dp.callback_query_handler(checking_meeting.filter(status="ok_good!"))
async def checking_meeting_ok_good(callback: CallbackQuery):
    await callback.answer(cache_time=10)

    user_telegram=callback.from_user.id
    response = getfeedbackfromuser(user_telegram)

    if response.status_code == 200:
        if response.json() == 'false':
            await callback.message.answer('Замечательно✨ Как бы ты оценил встречу?', reply_markup=leave_feedback_buttons(meeting_feedback))

        elif response.json() == 'true':
            await callback.message.answer('Твой собеседник уже оценил встречу. А что думаешь ты?', reply_markup=leave_feedback_buttons(meeting_feedback))




@dp.callback_query_handler(checking_meeting.filter(status="not_answer"))
async def checking_meeting_not_answer(callback: CallbackQuery):
    await callback.answer(cache_time=10)

    text = """Хочешь ли ты поменять его?
Или пока подождать ответа?🧙‍♂️"""

    a = InlineKeyboardMarkup(
        row_width=2,
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text='Я подожду',
                    callback_data=checking_meeting.new(status="I_wait"),

                ),
                InlineKeyboardButton(
                    text='Хочу поменять',
                    callback_data=checking_meeting.new(status="want_change_partner")

                ),

            ]
        ]
    )
    await callback.message.answer(text, reply_markup=a)


@dp.callback_query_handler(checking_meeting.filter(status="I_wait"))
async def checking_meeting_I_wait(callback: CallbackQuery):
    await callback.answer(cache_time=10)

    text = """Хорошо, мы дали знать ему об этом📩
    """
    await callback.message.answer(text)


@dp.callback_query_handler(checking_meeting.filter(status="want_change_partner"))
async def checking_meeting_status_change_partner(callback: CallbackQuery):
    await callback.answer(cache_time=10)

    text = """"Ты всегда можешь взять больше, чем ничего".
Мы постараемся найти тебе нового собеседника🕵️"""

    await callback.message.answer(text)

    profile_telegram = callback.from_user.id
    response = stop_meet_change_partner(profile_telegram, machine_token_constant)