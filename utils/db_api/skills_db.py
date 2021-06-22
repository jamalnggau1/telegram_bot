import sqlite3


class skills_db:
    def __init__(self, path_to_db="data/skills_categories_db.db"):
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

    def create_table_skills_categories(self):
        sql = """
           CREATE TABLE Skills_Categories(
           skill_category_id int NOT NULL,
           category_name varchar(255) NOT NULL      
           );
           """
        self.execute(sql, commit=True)



def loggg(statement):
    print(
        f"""
        -------------------------------
        {statement}
        -------------------------------
    """
    )