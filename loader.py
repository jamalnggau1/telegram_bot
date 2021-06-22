from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import config
from utils.db_api.Users_db import DataBase
from utils.db_api.SkillsCategories_db import SkillsCategories


bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
users_db = DataBase()
skills_categories_db = SkillsCategories()
