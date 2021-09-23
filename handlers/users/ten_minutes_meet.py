from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command

from keyboards.inline.callback_data import change_meeting_status_callback
from keyboards.inline.inline_buttons import one_button
from loader import dp


@dp.message_handler(Command("fast_meet"))
async def fast_meet_start(message: types.Message, state: FSMContext):
    await message.answer("🧙‍♀️ В тот же миг Алиса юркнула за ним следом, не думая о том, как же она будет выбираться обратно.",
                         reply_markup=one_button(text_btn="🔮 перейти к 10-минутным встречам 🧙‍♀️",
                                                 callback_data=change_meeting_status_callback.new(status="10"),
                                                 url='t.me/EvgTG_bot?start=666'))