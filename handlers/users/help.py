from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Список команд: ",
            "/start - Запуск бота",
            "/profile - Информауия о твоем профиле",
            "/help - Получить справку",
            "/meett - Выбрать тип встречи")
    
    await message.answer("\n".join(text))
