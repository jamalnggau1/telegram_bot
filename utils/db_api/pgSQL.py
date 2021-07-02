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
                          contacts: list[str] = None, language: str = None):
        sql = """INSERT INTO public.filling_profile_profile(full_name, email) 
                    VALUES($1,$2) """
        await self.pool.execute(sql, full_name, email)

    async def select_profile(self,
                             **kwargs):  # Запрос из БД происходит в формате select_profile(full_name='...', id = ...)
        sql = """SELECT * FROM public.filling_profile_profile WHERE """
        sql, parameters = self.format_args(sql, kwargs)
        return await self.pool.fetchrow(sql, *parameters)
