import time

import requests as requests
from aiogram.types import CallbackQuery

from constants import host, machine_token_constant
from keyboards.inline.callback_data import no_email_flow, \
    edite_profile_callback
from keyboards.inline.inline_buttons import one_button
from loader import dp
from request_to_server.requests import login
from request_to_server.requests import registration


@dp.callback_query_handler(no_email_flow.filter(status="step_1"))
async def meeting_status_waiting(callback: CallbackQuery):
    await callback.answer(cache_time=10)
    telegram_id = callback.from_user.id
    full_name = callback.from_user.full_name

    await callback.message.answer("""📆Каждую неделю я буду присылать собеседников в соответствии с твоими интересами.

🔄Взамен тебе нужно лишь написать им и не ждать, что они сделают это за тебя (помни про равноценный обмен).

<i>«А зачем кому-то знать мои интересы?»</i>
– произнёс твой внутренний голос.""")

    time.sleep(7)

    registration_response = registration(telegram_id, full_name, str(telegram_id))
    print(f'имя:{full_name}, telegram: {telegram_id}, registration_response.status_code: {registration_response.status_code}')
    if registration_response.status_code == 201:

        url = host + '/filling_profile/'
        await callback.message.answer("""<b>На это есть две важные причины:</b>

🎯Это нужно для того, чтобы мы нашли человека, интересы которого будут полностью или частично совпадать с твоими. Так ты всегда сможешь найти общие темы для разговора.

🙇‍♂️А еще ты должен помнить, что все люди разные и некоторым сложно решиться на встречу с человеком, о котором ничего не знаешь.

Возможно, кто-то уже ждет тебя?👀""",
                                      reply_markup=one_button(
                                          text_btn="Указать интересы",
                                          callback_data=edite_profile_callback.new(status="edite_profile"),
                                          url=requests.post(url, params={
                                              'token': login(telegram_id, machine_token_constant).json().get("token"),
                                              'contacts': telegram_id}).url
                                      )
                                      )
    else:
        await callback.message.answer("""ты не зареган.""")

