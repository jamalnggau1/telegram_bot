from aiogram.types import InlineKeyboardMarkup
from aiogram.utils import callback_data
from aiogram.utils.callback_data import CallbackData

from utils.db_api.SkillsCategories_db import SkillsCategories

show_categories = CallbackData("show_categories")
show_skills = CallbackData("show_skills", "category_name")


async def categories_keyboard():
    markup = InlineKeyboardMarkup()
    all_categories = SkillsCategories.get_categories()

    for i in all_categories:
        markup.insert(
            InlineKeyboardMarkup(text=i[1], callback_data=show_categories)
        )

    return markup
