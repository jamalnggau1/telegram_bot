from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from constants import host, machine_token_constant
from enum_constans import want_find_another_companion, thank_you_for_feedback_see_you_on_Sunday, see_you_on_Sunday, \
    impossible_to_leave_feedback, your_profile_is_empty, change_profile
from keyboards.inline.callback_data import meeting_feedback, change_meeting_status_callback, edite_profile_callback
from keyboards.inline.inline_buttons import two_buttons, one_button
from loader import dp
from request_to_server.requests import leave_feedback, login
import requests as requests
from utils.filling_skills_check import filling_skills_check


@dp.callback_query_handler(meeting_feedback.filter(status="1"))
async def leave_feedback_1(callback: CallbackQuery, state: FSMContext):
    await callback.answer(cache_time=10)
    telegram_id = callback.from_user.id

    response = leave_feedback(telegram_id, machine_token_constant, 1)
    if response.status_code == 200:
        if filling_skills_check(telegram_id) == "Error":
            await callback.message.answer("У нас возникла ошибка, связанная с заполнением твоего профиля. Пожалуйста, обратись в поддержку, на писав /help.")
        elif filling_skills_check(telegram_id) is True:
            await callback.message.answer(
                text=want_find_another_companion,
                reply_markup=two_buttons(
                    first_button_text="Да",
                    first_button_callback=change_meeting_status_callback.new(status="change_meeting_status"),
                    second_button_text="Нет",
                    second_button_callback=change_meeting_status_callback.new(status="ничего не делаем")))
        elif filling_skills_check(telegram_id) is False:
            url = host + '/filling_profile/'
            await callback.message.answer(
                text=your_profile_is_empty,
                reply_markup=one_button(
                    text_btn=change_profile,
                    callback_data=edite_profile_callback.new(status="edite_profile"),
                    url=requests.post(
                        url=url,
                        params={'token': login(telegram_id, machine_token_constant).json().get("token"),
                                'contacts': telegram_id}).url
                )
            )

    else:
        await callback.message.answer(impossible_to_leave_feedback)



@dp.callback_query_handler(meeting_feedback.filter(status="2"))
async def leave_feedback_2(callback: CallbackQuery):
    await callback.answer(cache_time=10)
    telegram_id = callback.from_user.id
    response = leave_feedback(telegram_id, machine_token_constant, 2)
    if response.status_code == 200:
        if filling_skills_check(telegram_id) == "Error":
            await callback.message.answer("У нас возникла ошибка, связанная с заполнением твоего профиля. Пожалуйста, обратись в поддержку, на писав /help.")
        elif filling_skills_check(telegram_id) is True:
            await callback.message.answer(
                text=want_find_another_companion,
                reply_markup=two_buttons(
                    first_button_text="Да",
                    first_button_callback=change_meeting_status_callback.new(status="change_meeting_status"),
                    second_button_text="Нет",
                    second_button_callback=change_meeting_status_callback.new(status="ничего не делаем")))
        elif filling_skills_check(telegram_id) is False:
            url = host + '/filling_profile/'
            await callback.message.answer(
                text=your_profile_is_empty,
                reply_markup=one_button(
                    text_btn=change_profile,
                    callback_data=edite_profile_callback.new(status="edite_profile"),
                    url=requests.post(
                        url=url,
                        params={'token': login(telegram_id, machine_token_constant).json().get("token"),
                                'contacts': telegram_id}).url
                )
            )

    else:
        await callback.message.answer(impossible_to_leave_feedback)


@dp.callback_query_handler(meeting_feedback.filter(status="3"))
async def leave_feedback_3(callback: CallbackQuery):
    await callback.answer(cache_time=10)
    telegram_id = callback.from_user.id

    response = leave_feedback(telegram_id, machine_token_constant, 3)
    if response.status_code == 200:
        if filling_skills_check(telegram_id) == "Error":
            await callback.message.answer("У нас возникла ошибка, связанная с заполнением твоего профиля. Пожалуйста, обратись в поддержку, на писав /help.")
        elif filling_skills_check(telegram_id) is True:
            await callback.message.answer(
                text=want_find_another_companion,
                reply_markup=two_buttons(
                    first_button_text="Да",
                    first_button_callback=change_meeting_status_callback.new(status="change_meeting_status"),
                    second_button_text="Нет",
                    second_button_callback=change_meeting_status_callback.new(status="ничего не делаем")))
        elif filling_skills_check(telegram_id) is False:
            url = host + '/filling_profile/'
            await callback.message.answer(
                text=your_profile_is_empty,
                reply_markup=one_button(
                    text_btn=change_profile,
                    callback_data=edite_profile_callback.new(status="edite_profile"),
                    url=requests.post(
                        url=url,
                        params={'token': login(telegram_id, machine_token_constant).json().get("token"),
                                'contacts': telegram_id}).url
                )
            )

    else:
        await callback.message.answer(impossible_to_leave_feedback)


@dp.callback_query_handler(meeting_feedback.filter(status="4"))
async def leave_feedback_4(callback: CallbackQuery):
    await callback.answer(cache_time=10)
    telegram_id = callback.from_user.id
    response = leave_feedback(telegram_id, machine_token_constant, 4)
    if response.status_code == 200:
        if filling_skills_check(telegram_id) == "Error":
            await callback.message.answer("У нас возникла ошибка, связанная с заполнением твоего профиля. Пожалуйста, обратись в поддержку, на писав /help.")
        elif filling_skills_check(telegram_id) is True:
            await callback.message.answer(
                text=want_find_another_companion,
                reply_markup=two_buttons(
                    first_button_text="Да",
                    first_button_callback=change_meeting_status_callback.new(status="change_meeting_status"),
                    second_button_text="Нет",
                    second_button_callback=change_meeting_status_callback.new(status="ничего не делаем")))
        elif filling_skills_check(telegram_id) is False:
            url = host + '/filling_profile/'
            await callback.message.answer(
                text=your_profile_is_empty,
                reply_markup=one_button(
                    text_btn=change_profile,
                    callback_data=edite_profile_callback.new(status="edite_profile"),
                    url=requests.post(
                        url=url,
                        params={'token': login(telegram_id, machine_token_constant).json().get("token"),
                                'contacts': telegram_id}).url
                )
            )

    else:
        await callback.message.answer(impossible_to_leave_feedback)


@dp.callback_query_handler(meeting_feedback.filter(status="5"))
async def leave_feedback_4(callback: CallbackQuery):
    await callback.answer(cache_time=10)
    telegram_id = callback.from_user.id
    response = leave_feedback(telegram_id, machine_token_constant, 5)
    if response.status_code == 200:
        if filling_skills_check(telegram_id) == "Error":
            await callback.message.answer("У нас возникла ошибка, связанная с заполнением твоего профиля. Пожалуйста, обратись в поддержку, на писав /help.")
        elif filling_skills_check(telegram_id) is True:
            await callback.message.answer(
                text=want_find_another_companion,
                reply_markup=two_buttons(
                    first_button_text="Да",
                    first_button_callback=change_meeting_status_callback.new(status="change_meeting_status"),
                    second_button_text="Нет",
                    second_button_callback=change_meeting_status_callback.new(status="ничего не делаем")))
        elif filling_skills_check(telegram_id) is False:
            url = host + '/filling_profile/'
            await callback.message.answer(
                text=your_profile_is_empty,
                reply_markup=one_button(
                    text_btn=change_profile,
                    callback_data=edite_profile_callback.new(status="edite_profile"),
                    url=requests.post(
                        url=url,
                        params={'token': login(telegram_id, machine_token_constant).json().get("token"),
                                'contacts': telegram_id}).url
                )
            )

    else:
        await callback.message.answer(impossible_to_leave_feedback)





@dp.callback_query_handler(change_meeting_status_callback.filter(status="ничего не делаем"))
async def do_nothing(callback: CallbackQuery):
    await callback.answer(cache_time=10)

    await callback.message.answer(see_you_on_Sunday)





@dp.callback_query_handler(meeting_feedback.filter(status="1_saturday"))
async def leave_feedback_1(callback: CallbackQuery, state: FSMContext):
    await callback.answer(cache_time=10)
    telegram_id = callback.from_user.id
    response = leave_feedback(telegram_id, machine_token_constant, 1)
    if response.status_code == 200:
        await callback.message.answer(thank_you_for_feedback_see_you_on_Sunday)
    else:
        await callback.message.answer(impossible_to_leave_feedback)



@dp.callback_query_handler(meeting_feedback.filter(status="2_saturday"))
async def leave_feedback_2(callback: CallbackQuery):
    await callback.answer(cache_time=10)
    telegram_id = callback.from_user.id
    response = leave_feedback(telegram_id, machine_token_constant, 2)
    if response.status_code == 200:
        await callback.message.answer(thank_you_for_feedback_see_you_on_Sunday)
    else:
        await callback.message.answer(impossible_to_leave_feedback)


@dp.callback_query_handler(meeting_feedback.filter(status="3_saturday"))
async def leave_feedback_3(callback: CallbackQuery):
    await callback.answer(cache_time=10)
    telegram_id = callback.from_user.id
    response = leave_feedback(telegram_id, machine_token_constant, 3)
    if response.status_code == 200:
        await callback.message.answer(thank_you_for_feedback_see_you_on_Sunday)
    else:
        await callback.message.answer(impossible_to_leave_feedback)


@dp.callback_query_handler(meeting_feedback.filter(status="4_saturday"))
async def leave_feedback_4(callback: CallbackQuery):
    await callback.answer(cache_time=10)
    telegram_id = callback.from_user.id
    response = leave_feedback(telegram_id, machine_token_constant, 4)
    if response.status_code == 200:
        await callback.message.answer(thank_you_for_feedback_see_you_on_Sunday)
    else:
        await callback.message.answer(impossible_to_leave_feedback)


@dp.callback_query_handler(meeting_feedback.filter(status="5_saturday"))
async def leave_feedback_4(callback: CallbackQuery):
    await callback.answer(cache_time=10)
    telegram_id = callback.from_user.id
    response = leave_feedback(telegram_id, machine_token_constant, 5)
    if response.status_code == 200:
        await callback.message.answer(thank_you_for_feedback_see_you_on_Sunday)
    else:
        await callback.message.answer(impossible_to_leave_feedback)









