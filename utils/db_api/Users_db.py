import sqlite3


class DataBase:
    def __init__(self, path_to_db="data/main.db"):
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

    def create_table_users(self):
        sql = """
        CREATE TABLE Users(
        id int NOT NULL,
        full_name varchar(255) ,
        e_mail varchar(255)       
        );
        """
        self.execute(sql, commit=True)

    def add_user(self, id: int, full_name: str, e_mail: str):
        sql = "INSERT INTO Users(id,full_name,e_mail) VALUES(?,?,?)"
        parametrs = (id, full_name, e_mail)
        self.execute(sql, parametrs, commit=True)

    def select_all_users(self):
        sql = "SELECT * FROM Users"
        return self.execute(sql, fetchall=True)

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM Users;", fetchone=True)

    @staticmethod
    def format_args(sql, parametrs: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parametrs
        ])
        return sql, tuple(parametrs.values())

    def select_user(self, id):
        sql = f"SELECT * FROM Users WHERE id={id}"

        return self.execute(sql, fetchone=True)


def loggg(statement):
    print(
        f"""
        -------------------------------
        {statement}
        -------------------------------
    """
    )
