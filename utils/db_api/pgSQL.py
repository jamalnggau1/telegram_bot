import datetime
from typing import Union

import asyncpg
from asyncpg import Pool
from data import config


class pgDataBase:
    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create(self):
        pool = await asyncpg.create_pool(
            user=config.PGUSER,
            password=config.PGPASSWORD,
            host=config.IP,
            database=config.DATABASE
        )
        self.pool = pool

    @staticmethod
    def format_args(sql, parametrs: dict):
        sql += " AND ".join([
            f"{item}=${num}" for num, item in enumerate(parametrs, start=1)
        ])
        return sql, tuple(parametrs.values())

    async def add_profile(self, full_name: str, email: str = None, skills: list[int] = None, goal: int = None,
                          contacts: str = None, language: str = None, meeting_status='not ready'):
        sql = """INSERT INTO public.filling_profile_profile(full_name, email, contacts, meeting_status) 
                    VALUES($1,$2,$3,$4) """
        await self.pool.execute(sql, full_name, email,contacts,meeting_status)

    async def add_meet(self, first_profile_id, second_profile_id: int, date_meeting: datetime = None):
        sql = """INSERT INTO public.filling_profile_meet(first_profile_id, second_profile_id,date_meeting) 
                       VALUES($1,$2,$3) """
        await self.pool.execute(sql, first_profile_id, second_profile_id, date_meeting)

    async def delete_all_from_meet(self):
        sql = "DELETE FROM public.filling_profile_meet"
        await self.pool.execute(sql)

    # Запрос из БД происходит в формате select_profile(full_name='...', id = ...)
    async def select_profile(self, **kwargs):
        sql = """SELECT * FROM public.filling_profile_profile WHERE """
        sql, parameters = self.format_args(sql, kwargs)
        return await self.pool.fetchrow(sql, *parameters)

    async def select_all_profile(self):  # Получение всех профиоей из БД
        sql = "SELECT * FROM public.filling_profile_profile"
        return await self.pool.fetch(sql)

    async def count_profile(self):  # Получение всех профиоей из БД
        sql = "SELECT COUNT(*) FROM public.filling_profile_profile"
        return await self.pool.fetchval(sql)

    # добавляет пользователя в таблицу из которой будет осуществляться поиск пары
    async def add_profile_for_meetting(self, profile_id: int):
        sql = """INSERT INTO public.filling_profile_profile_for_metting(profile_id) 
                    VALUES($1) """
        await self.pool.execute(sql, profile_id)

    async def update_profile_meeting_status(self, meeting_status, full_name):
        sql = """UPDATE public.filling_profile_profile SET meeting_status =$1 WHERE full_name=$2"""

        await self.pool.execute(sql, meeting_status, full_name)

    async def select_profile_for_meeting(self, profile_id):
        sql = """SELECT * FROM public.filling_profile_profile_for_metting WHERE profile_id=$1"""
        return await self.pool.fetchrow(sql, profile_id)

    async def select_all_profiles_for_meeting(self):
        sql = """SELECT * FROM public.filling_profile_profile_for_metting """
        return await self.pool.fetch(sql)

    async def delete_profile_for_meeting(self, profile_id):
        sql = "DELETE FROM public.filling_profile_profile_for_metting WHERE profile_id=$1"
        await self.pool.execute(sql, profile_id)

    async def select_meet_list(self, profile_id):
        sql = """SELECT * FROM public.filling_profile_meet WHERE first_profile_id=$1"""
        return await self.pool.fetch(sql, profile_id)
