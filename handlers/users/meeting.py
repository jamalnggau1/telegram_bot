from aiogram.types import CallbackQuery

import constants
from enum_constans import meeting_status_constant, waiting_status_constant, not_ready_status_constant, see_you_in_week, \
    find_companion_on_Monday, error_contact_support
from keyboards.inline.callback_data import change_meeting_status_callback, meeting_status_callback
from loader import dp
from request_to_server.requests import patch, login


@dp.callback_query_handler(change_meeting_status_callback.filter(status="change_meeting_status"))
async def change_meeting_status(callback: CallbackQuery):
    await callback.answer(cache_time=10)

    current_meeting_status = int(login(callback.from_user.id, constants.machine_token_constant).json().get("meeting_status"))
    token = login(callback.from_user.id, constants.machine_token_constant).json().get("token")

    if current_meeting_status == waiting_status_constant:
        await callback.message.answer("""Тогда, надеюсь, увидимся в воскресенье, когда мы начинаем неделю новых встреч📬""")
        patch(not_ready_status_constant, token)


    elif current_meeting_status == not_ready_status_constant:
        await callback.message.answer("""Тогда мы начнем поиск немедля. Скоро вернемся с новым собеседником⏰""")
        patch(waiting_status_constant, token)



# Используется в воскресенье, когда нужно в любом случае поставить статус waiting
@dp.callback_query_handler(meeting_status_callback.filter(status="meeting_status = waiting"))
async def meeting_status_waiting(callback: CallbackQuery):
    await callback.answer(cache_time=10)

    token = login(callback.from_user.id, constants.machine_token_constant).json().get("token")

    if patch(waiting_status_constant, token) == 200:
        await callback.message.answer(find_companion_on_Monday)

    else:
        await callback.message.answer(error_contact_support)


# Используется в воскресенье, когда нужно в любом случае поставить статус not ready
@dp.callback_query_handler(meeting_status_callback.filter(status="meeting_status = not ready"))
async def meeting_status_not_ready(callback: CallbackQuery):
    await callback.answer(cache_time=10)

    token = login(callback.from_user.id, constants.machine_token_constant).json().get("token")

    if patch(not_ready_status_constant, token) == 200:
        await callback.message.answer(see_you_in_week)

    else:
        await callback.message.answer(error_contact_support)
