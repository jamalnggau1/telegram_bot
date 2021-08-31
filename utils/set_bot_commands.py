from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("profile", "Информауия о твоем профиле"),
            types.BotCommand("help", "Вывести справку"),
            types.BotCommand("fast_meet", "Быстрая встреча"),

        ]
    )
