import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

BOT_TOKEN = os.getenv("BOT_TOKEN")
DOSTAVKA_HOST = os.getenv("DOSTAVKA_HOST")
DOSTAVKA_PORT = os.getenv("DOSTAVKA_PORT")
