from aiogram.types import CallbackQuery

import constants
from keyboards.inline.callback_data import meeting_feedback
from loader import dp
from request_to_server.requests import leave_feedback


@dp.callback_query_handler(meeting_feedback.filter(status="1"))
async def reg_bot(callback: CallbackQuery):
    await callback.answer(cache_time=10)

    response = leave_feedback(callback.from_user.id, constants.a, '👎')
    if response.status_code == 200:
        await callback.answer('Твой отзыв о встрече оставлен')
    else:
        await callback.answer('Невозможно оставить отзыв, обратитесь в поддержку жи есть')

@dp.callback_query_handler(meeting_feedback.filter(status="2"))
async def reg_bot(callback: CallbackQuery):
    await callback.answer(cache_time=10)

    response = leave_feedback(callback.from_user.id, constants.a, '😒')
    if response.status_code == 200:
        await callback.answer('Твой отзыв о встрече оставлен')
    else:
        await callback.answer('Невозможно оставить отзыв, обратитесь в поддержку жи есть')

@dp.callback_query_handler(meeting_feedback.filter(status="3"))
async def reg_bot(callback: CallbackQuery):
    await callback.answer(cache_time=10)

    response = leave_feedback(callback.from_user.id, constants.a, '🙂')
    if response.status_code == 200:
        await callback.answer('Твой отзыв о встрече оставлен')
    else:
        await callback.answer('Невозможно оставить отзыв, обратитесь в поддержку жи есть')

@dp.callback_query_handler(meeting_feedback.filter(status="4"))
async def reg_bot(callback: CallbackQuery):
    await callback.answer(cache_time=10)

    response = leave_feedback(callback.from_user.id, constants.a, '😍')
    if response.status_code == 200:
        await callback.answer('Твой отзыв о встрече оставлен')
    else:
        await callback.answer('Невозможно оставить отзыв, обратитесь в поддержку жи есть')

@dp.callback_query_handler(meeting_feedback.filter(status="5"))
async def reg_bot(callback: CallbackQuery):
    await callback.answer(cache_time=10)

    response = leave_feedback(callback.from_user.id, constants.a, '👍')
    if response.status_code == 200:
        await callback.answer('Твой отзыв о встрече оставлен')
    else:
        await callback.answer('Невозможно оставить отзыв, обратитесь в поддержку жи есть')
