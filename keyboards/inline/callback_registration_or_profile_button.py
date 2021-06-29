from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_data import registration_callback


regestration_or_profile_button = InlineKeyboardMarkup(
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