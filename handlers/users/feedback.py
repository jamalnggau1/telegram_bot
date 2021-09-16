from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

import constants
from enum_constans import want_find_another_companion, thank_you_for_feedback_see_you_on_Sunday, see_you_on_Sunday
from keyboards.inline.callback_data import meeting_feedback, change_meeting_status_callback
from keyboards.inline.inline_buttons import two_buttons
from loader import dp
from request_to_server.requests import leave_feedback
from states import Meeting_states, Registration_states


@dp.callback_query_handler(meeting_feedback.filter(status="1"))
async def leave_feedback_1(callback: CallbackQuery, state: FSMContext):
    await callback.answer(cache_time=10)

    response = leave_feedback(callback.from_user.id, constants.a, '👎')
    if response.status_code == 200:
        await callback.message.answer(want_find_another_companion,reply_markup=two_buttons("Да",change_meeting_status_callback.new(status="change_meeting_status"),"Нет",change_meeting_status_callback.new(status="ничего не делаем")))
    else:
        await callback.message.answer('Невозможно оставить отзыв, обратитесь в поддержку жи есть')



@dp.callback_query_handler(meeting_feedback.filter(status="2"))
async def leave_feedback_2(callback: CallbackQuery):
    await callback.answer(cache_time=10)

    response = leave_feedback(callback.from_user.id, constants.a, '😒')
    if response.status_code == 200:
        await callback.message.answer(want_find_another_companion, reply_markup=two_buttons("Да",
                                                                                                                change_meeting_status_callback.new(
                                                                                                                    status="change_meeting_status"),
                                                                                                                "Нет",
                                                                                                                change_meeting_status_callback.new(
                                                                                                                    status="ничего не делаем")))
    else:
        await callback.message.answer('Невозможно оставить отзыв, обратитесь в поддержку жи есть')


@dp.callback_query_handler(meeting_feedback.filter(status="3"))
async def leave_feedback_3(callback: CallbackQuery):
    await callback.answer(cache_time=10)

    response = leave_feedback(callback.from_user.id, constants.a, '🙂')
    if response.status_code == 200:
        await callback.message.answer(want_find_another_companion, reply_markup=two_buttons("Да",
                                                                                                                change_meeting_status_callback.new(
                                                                                                                    status="change_meeting_status"),
                                                                                                                "Нет",
                                                                                                                change_meeting_status_callback.new(
                                                                                                                    status="ничего не делаем")))
    else:
        await callback.message.answer('Невозможно оставить отзыв, обратитесь в поддержку жи есть')


@dp.callback_query_handler(meeting_feedback.filter(status="4"))
async def leave_feedback_4(callback: CallbackQuery):
    await callback.answer(cache_time=10)

    response = leave_feedback(callback.from_user.id, constants.a, '😍')
    if response.status_code == 200:
        await callback.message.answer(want_find_another_companion, reply_markup=two_buttons("Да",
                                                                                                                change_meeting_status_callback.new(
                                                                                                                    status="change_meeting_status"),
                                                                                                                "Нет",
                                                                                                                change_meeting_status_callback.new(
                                                                                                                    status="ничего не делаем")))
    else:
        await callback.message.answer('Невозможно оставить отзыв, обратитесь в поддержку жи есть')


@dp.callback_query_handler(meeting_feedback.filter(status="5"))
async def leave_feedback_4(callback: CallbackQuery):
    await callback.answer(cache_time=10)

    response = leave_feedback(callback.from_user.id, constants.a, '👍')
    if response.status_code == 200:
        await callback.message.answer(want_find_another_companion, reply_markup=two_buttons("Да",
                                                                                                                change_meeting_status_callback.new(
                                                                                                                    status="change_meeting_status"),
                                                                                                                "Нет",
                                                                                                                change_meeting_status_callback.new(
                                                                                                                    status="ничего не делаем")))
    else:
        await callback.message.answer('Невозможно оставить отзыв, обратитесь в поддержку жи есть')





@dp.callback_query_handler(change_meeting_status_callback.filter(status="ничего не делаем"))
async def do_nothing(callback: CallbackQuery):
    await callback.answer(cache_time=10)

    await callback.message.answer(see_you_on_Sunday)





@dp.callback_query_handler(meeting_feedback.filter(status="1_saturday"))
async def leave_feedback_1(callback: CallbackQuery, state: FSMContext):
    await callback.answer(cache_time=10)

    response = leave_feedback(callback.from_user.id, constants.a, '👎')
    if response.status_code == 200:
        await callback.message.answer(thank_you_for_feedback_see_you_on_Sunday)
    else:
        await callback.message.answer('Невозможно оставить отзыв, обратитесь в поддержку жи есть')



@dp.callback_query_handler(meeting_feedback.filter(status="2_saturday"))
async def leave_feedback_2(callback: CallbackQuery):
    await callback.answer(cache_time=10)

    response = leave_feedback(callback.from_user.id, constants.a, '😒')
    if response.status_code == 200:
        await callback.message.answer(thank_you_for_feedback_see_you_on_Sunday)
    else:
        await callback.message.answer('Невозможно оставить отзыв, обратитесь в поддержку жи есть')


@dp.callback_query_handler(meeting_feedback.filter(status="3_saturday"))
async def leave_feedback_3(callback: CallbackQuery):
    await callback.answer(cache_time=10)

    response = leave_feedback(callback.from_user.id, constants.a, '🙂')
    if response.status_code == 200:
        await callback.message.answer(thank_you_for_feedback_see_you_on_Sunday)
    else:
        await callback.message.answer('Невозможно оставить отзыв, обратитесь в поддержку жи есть')


@dp.callback_query_handler(meeting_feedback.filter(status="4_saturday"))
async def leave_feedback_4(callback: CallbackQuery):
    await callback.answer(cache_time=10)

    response = leave_feedback(callback.from_user.id, constants.a, '😍')
    if response.status_code == 200:
        await callback.message.answer(thank_you_for_feedback_see_you_on_Sunday)
    else:
        await callback.message.answer('Невозможно оставить отзыв, обратитесь в поддержку жи есть')


@dp.callback_query_handler(meeting_feedback.filter(status="5_saturday"))
async def leave_feedback_4(callback: CallbackQuery):
    await callback.answer(cache_time=10)

    response = leave_feedback(callback.from_user.id, constants.a, '👍')
    if response.status_code == 200:
        await callback.message.answer(thank_you_for_feedback_see_you_on_Sunday)
    else:
        await callback.message.answer('Невозможно оставить отзыв, обратитесь в поддержку жи есть')









