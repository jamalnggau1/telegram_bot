from typing import Union

import asyncpg
import psycopg2
from asyncpg import Pool
from psycopg2 import Error
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

    async def add_user(self):
        sql = """INSERT INTO public."Profile"(id,full_name, email, skills) VALUES(1,'Dmitry Shvicov','gusi@mail.ru','{1,6,12}')"""
        await self.pool.execute(sql)

