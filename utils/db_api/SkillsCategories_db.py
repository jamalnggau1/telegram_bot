import sqlite3


class SkillsCategories:
    def __init__(self, path_to_db="data/SkillsCategories.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parametrs: tuple = None, fetchone=False, fetchall=False, commit=False):

        if not parametrs:
            parametrs = tuple()
        connection = self.connection
        cursor = connection.cursor()
        cursor.execute(sql, parametrs)
        connection.set_trace_callback(loggg)
        data = None
        if commit:
            connection.commit()
        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data = cursor.fetchall()
        connection.close()
        return data

    def create_table_categories(self):
        sql = """
            CREATE TABLE Categories(
            id int NOT NULL,
            full_name varchar(255)       
            );
        """
        self.execute(sql, commit=True)

    def create_table_skills(self):
        sql = """
            CREATE TABLE Skills(
            id_category int NOT NULL,
            id_skills int NOT NULL,
            full_name varchar(255)
                   
            );
        """
        self.execute(sql, commit=True)

    def add_categories(self, id: int, full_name: str):
        sql = "INSERT INTO Categories(id,full_name) VALUES(?,?)"
        parametrs = (id, full_name)
        self.execute(sql, parametrs, commit=True)

    def add_skills(self, id_category: int,id_skills: int, full_name: str):
        sql = "INSERT INTO Skills(id_category,id_skills, full_name) VALUES(?,?,?)"
        parametrs = (id_category,id_skills, full_name)
        self.execute(sql, parametrs, commit=True)

def loggg(statement):
    print(
        f"""
            -------------------------------
            {statement}
            -------------------------------
        """
    )
