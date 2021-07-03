from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_data import registration_callback, edite_profile_callback

regestration_button = InlineKeyboardMarkup(
    row_width=1,
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="регистрация",
                callback_data=registration_callback.new(status="reg")

            )
        ]
    ]
)

edite_profile_button = InlineKeyboardMarkup(
    row_width=1,
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="изменить профиль",
                callback_data=edite_profile_callback.new(status="edite_profile"),
                url='http://127.0.0.1:8000/filling_profile/'



            )
        ]
    ]
)