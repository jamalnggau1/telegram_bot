from aiogram.types import CallbackQuery

import constants
from keyboards.inline.callback_data import meeting_feedback
from loader import dp
from request_to_server.requests import leave_feedback


@dp.callback_query_handler(meeting_feedback.filter(status="1"))
async def leave_feedback_1(callback: CallbackQuery):
    await callback.answer(cache_time=10)

    response = leave_feedback(callback.from_user.id, constants.a, '👎')
    if response.status_code == 200:
        await callback.message.answer('Твой отзыв о встрече оставлен')
    else:
        await callback.message.answer('Невозможно оставить отзыв, обратитесь в поддержку жи есть')


@dp.callback_query_handler(meeting_feedback.filter(status="2"))
async def leave_feedback_2(callback: CallbackQuery):
    await callback.answer(cache_time=10)

    response = leave_feedback(callback.from_user.id, constants.a, '😒')
    if response.status_code == 200:
        await callback.message.answer('Твой отзыв о встрече оставлен')
    else:
        await callback.message.answer('Невозможно оставить отзыв, обратитесь в поддержку жи есть')


@dp.callback_query_handler(meeting_feedback.filter(status="3"))
async def leave_feedback_3(callback: CallbackQuery):
    await callback.answer(cache_time=10)

    response = leave_feedback(callback.from_user.id, constants.a, '🙂')
    if response.status_code == 200:
        await callback.message.answer('Твой отзыв о встрече оставлен')
    else:
        await callback.message.answer('Невозможно оставить отзыв, обратитесь в поддержку жи есть')


@dp.callback_query_handler(meeting_feedback.filter(status="4"))
async def leave_feedback_4(callback: CallbackQuery):
    await callback.answer(cache_time=10)

    response = leave_feedback(callback.from_user.id, constants.a, '😍')
    if response.status_code == 200:
        await callback.message.answer('Твой отзыв о встрече оставлен')
    else:
        await callback.message.answer('Невозможно оставить отзыв, обратитесь в поддержку жи есть')


@dp.callback_query_handler(meeting_feedback.filter(status="5"))
async def leave_feedback_5(callback: CallbackQuery):
    await callback.answer(cache_time=10)

    response = leave_feedback(callback.from_user.id, constants.a, '👍')
    if response.status_code == 200:
        await callback.message.answer('Твой отзыв о встрече оставлен')
    else:
        await callback.message.answer('Невозможно оставить отзыв, обратитесь в поддержку жи есть')
