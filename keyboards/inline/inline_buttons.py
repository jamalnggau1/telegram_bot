from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_data import change_meeting_status_callback, edite_profile_callback, \
    meeting_status_callback, help_callbackdata, meeting_feedback


def one_button(text_btn=None, callback_data=None, url=None):
    if url is None:
        return InlineKeyboardMarkup(
            row_width=1,
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text=text_btn,
                        callback_data=callback_data

                    )
                ]
            ]
        )
    else:
        return InlineKeyboardMarkup(
            row_width=1,
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text=text_btn,
                        callback_data=callback_data,
                        url=url
                    )
                ]
            ]
        )


def change_profile_or_status_button(text_btn1, url, text_btn2):
    return InlineKeyboardMarkup(
        row_width=2,
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=text_btn1,
                    callback_data=edite_profile_callback.new(status="edite_profile"),
                    url=url

                ),
                InlineKeyboardButton(
                    text=text_btn2,
                    callback_data=change_meeting_status_callback.new(status="change_meeting_status")

                )
            ]
        ]
    )


def meeting_status_button(text_btn1, text_btn2):
    return InlineKeyboardMarkup(
        row_width=1,
        inline_keyboard=[
            [

                InlineKeyboardButton(
                    text=text_btn1,
                    callback_data=meeting_status_callback.new(status="meeting_status = waiting"),

                )
            ],
            [
                InlineKeyboardButton(
                    text=text_btn2,
                    callback_data=meeting_status_callback.new(status="meeting_status = not ready"),

                )
            ],

        ]
    )


def help_keyboard():
    return InlineKeyboardMarkup(
        row_width=1,
        inline_keyboard=[
            [

                InlineKeyboardButton(
                    text="Как работает бот?",
                    callback_data=help_callbackdata.new(status="how_bot_working"),

                )
            ],
            [
                InlineKeyboardButton(
                    text="Подсказки для первой встречи",
                    callback_data=help_callbackdata.new(status="just"),

                )
            ],
            [
                InlineKeyboardButton(
                    text="Задай свой вопрос",
                    callback_data=help_callbackdata.new(status="ask_question"),

                )
            ],

        ]
    )

def leave_feedback_buttons():
    return InlineKeyboardMarkup(
        row_width=5,
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text='👎',
                    callback_data=meeting_feedback.new(status="1")

                ),
                InlineKeyboardButton(
                    text='😒',
                    callback_data=meeting_feedback.new(status="2")

                ),
                InlineKeyboardButton(
                    text='🙂',
                    callback_data=meeting_feedback.new(status="3")

                ),

                InlineKeyboardButton(
                    text='😍',
                    callback_data=meeting_feedback.new(status="4")
                ),
                InlineKeyboardButton(
                    text='👍',
                    callback_data=meeting_feedback.new(status="5")
                )

            ]
        ]
    )
