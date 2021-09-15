from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from keyboards.inline.callback_data import help_callbackdata
from keyboards.inline.inline_buttons import help_keyboard, meeting_status_button, one_button
from loader import dp, bot


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = "Здесь мы постараемся дать ответы на интересующие тебя вопросы. Что бы ты хотел узнать?"

    await message.answer(text, reply_markup=help_keyboard())


@dp.callback_query_handler(help_callbackdata.filter(status="just"))
async def help_message(callback: types.CallbackQuery):
    await callback.message.answer("""💡Подсказки для твоей первой встречи
            📆1) Когда ты получил собеседника, не стесняйся написать первым, сделать первый шаг навстречу - красивый и смелый жест.
            Начать можно так: Привет, бот BeNearly написал, что ты мой собеседник на этой неделе. Рад(а) познакомиться :)

            📭2)Что делать, если собеседник не отвечает?
            Такое случается, не унывай.
            Просто попробуй напомнить о себе в чате
            Например, вот так: Привет, что насчет нашей встречи? У тебя получится пообщаться на этой неделе?
            Но если собеседник по-прежнему не отвечает, то расскажи нам об этом в среду. Мы обязательно попытаемся найти тебе  нового собеседника, не переживай.🙌

            ⏳3)И, конечно же, старайся не игнорировать собеседника, лучше напиши сразу, если не получится пообщаться.

            🔮4)Ну а мы готовы ответить в любое время под звездами. Просто воспользуйся командой /help.""")


@dp.callback_query_handler(help_callbackdata.filter(status="how_bot_working"))
async def how_bot_working(callback: types.CallbackQuery):
    await callback.message.answer("""☯️Сейчас мы проводим встречи в двух разных форматах: недельные и 10-минутные встречи.

📆Недельные встречи: в начале недели мы подбираем тебе собеседника. В этом формате подбор осуществляется на основе интересов и целей, которые  пользователь указал в личном профиле.

По средам и субботам мы просим собеседников оценить, как прошла встреча. Это нужно для того, чтобы в дальнейшем формировать репутацию пользователей, что позволит тебе избегать неадекватных собеседников.🤹‍♂️

⏳10-минутные встречи:
Не раздумывая и не отвлекаясь на предрассудки,  случайных собеседников  просто подбрасывает  прямо в море - бух.

 Во время встречи  ты останешься наедине с собеседником в тайном чате,  у тебя будет возможность обменятся контактной информацией, если  собеседник тебя зацепил, или  в любой момент покинуть встречу, не дожидаясь  окончания 10 минут.🎬
""")


@dp.callback_query_handler(help_callbackdata.filter(status="ask_question"))
async def ask_question(callback: types.CallbackQuery):
    await callback.message.answer("""⬇️⬇️⬇️Вводи свой вопрос прям сюда⬇️⬇️⬇️""")
