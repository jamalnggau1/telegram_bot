from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Список команд: ",
            "/profile - Информауия о твоем профиле",
            "/help - Получить справку",
            "/fast_meet - Быстрая встреча")
    
    await message.answer("\n".join(text))
