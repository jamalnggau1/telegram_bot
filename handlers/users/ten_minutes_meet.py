from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command

from keyboards.inline.callback_data import change_meeting_status_callback
from keyboards.inline.inline_buttons import one_button
from loader import dp


@dp.message_handler(Command("fast_meet"))
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer("🧙‍♀️ В тот же миг Алиса юркнула за ним следом, не думая о том, как же она будет выбираться обратно.",
                         reply_markup=one_button(text_btn=" перейти к чат-боту с 10 минутными почтами",
                                                 callback_data=change_meeting_status_callback.new(status="10"),
                                                 url='t.me/fast_10_minute_meet_bot?start=666'))