from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from enum_constans import first_meet, how_bot_work, help_menu
from keyboards.inline.callback_data import help_callbackdata
from keyboards.inline.inline_buttons import help_keyboard
from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = help_menu

    await message.answer(text, reply_markup=help_keyboard())


@dp.callback_query_handler(help_callbackdata.filter(status="just"))
async def help_message(callback: types.CallbackQuery):
    await callback.message.answer(first_meet)


@dp.callback_query_handler(help_callbackdata.filter(status="how_bot_working"))
async def how_bot_working(callback: types.CallbackQuery):
    await callback.message.answer(how_bot_work)

