from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from keyboards.inline.callback_data import registration_callback
from loader import dp, db
from states import Registration_states


@dp.callback_query_handler(registration_callback.filter(status="reg"))
async def reg_bot(callback: CallbackQuery):
    await callback.answer(cache_time=10)

    await callback.message.answer(f"Ты решил зарегаться. Вводи электронную почту")

    await Registration_states.enter_email.set()


@dp.message_handler(state=Registration_states.enter_email)
async def enter_email(message: types.Message , state: FSMContext):

    email = message.text
    id = message.from_user.id
    full_name = message.from_user.full_name


    db.add_user(id, full_name, email)

    count_users = db.count_users()[0]
    all_us = db.select_all_users()
    await message.answer(f"Ты зарегестрирован. В базе таких как ты {count_users}:{all_us}. ")
    await state.finish()
