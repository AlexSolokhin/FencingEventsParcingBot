import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit('Переменные окружения не загружены: проверьте файл .env')
else:
    load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

DEFAULT_COMMANDS = (
    ('start', "Послать приветственное сообщение"),
    ('help', "Выводит справку по командам бота")
)

PAGES_LIST = [
    'https://vk.com/longsword_club',
]

KEYWORDS = [
    'турнир',
]
