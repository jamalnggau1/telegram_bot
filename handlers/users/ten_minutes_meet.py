from aiogram.dispatcher.filters.builtin import Command
from aiogram import types

from keyboards.inline.callback_data import change_meeting_status_callback
from loader import dp
from enum_constans import fast_meet_message, fast_meet_bot_url
from keyboards.inline.inline_buttons import one_button



@dp.message_handler(Command("fast_meet"))
async def fast_meet_start(message: types.Message):
    await message.answer(
        text=fast_meet_message,
        reply_markup=one_button(
            text_btn="🔮 перейти к 10-минутным встречам 🧙‍♀️",
            callback_data=change_meeting_status_callback.new(status="10"),
            url=fast_meet_bot_url
        )
    )
