import sqlite3

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.inline.callback_registration_or_profile_button import regestration_or_profile_button
from loader import dp, db


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer(f"Привет, {message.from_user.full_name}!")

    count_users = db.count_users()[0]
    all_us = db.select_all_users()
    user = db.select_user(message.from_user.id)

    if user is not None:
        await message.answer(f"Ты уже зарегестрирован. В базе таких как ты {count_users}: {all_us}")

    else:

        await message.answer(text="Ты не зарегестрирован. Жми  на Кнопку ниже",
                             reply_markup=regestration_or_profile_button)
