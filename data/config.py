from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
IP = env.str("ip")  # Тоже str, но для айпи адреса хоста

PGUSER = env.str("PGUSER")  # Логин для базы данных
PGPASSWORD = env.str("PGPASSWORD")  # Пароль для базы данных
DATABASE = env.str("DATABASE")


admins = [
    336006405,
]
