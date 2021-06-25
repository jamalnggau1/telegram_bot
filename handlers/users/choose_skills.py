from typing import Union

from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp




@dp.message_handler(Command("skills"))
async def choose_skills(message: types.Message):
    await list_categories(message)

async def list_categories(message: Union[types.Message, types.CallbackQuery]):
    markup = await categories_keyboard()
