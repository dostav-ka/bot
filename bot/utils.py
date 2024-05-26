import re

from telebot import types

from api_dostavka import update_order_status


def generate_inline_keyboard():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Мои заказы")
    markup.add(btn1)
    return markup


def generate_final_inline_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    finish_button = types.InlineKeyboardButton(text="Завершить", callback_data="completed")
    keyboard.add(finish_button)
    return keyboard


def extract_order_id(message):
    match = re.search(r'#id (\d+)', message)
    if match:
        return match.group(1)
    else:
        return None


def change_status(order_id, user_id, status):
    id = extract_order_id(order_id)
    response = update_order_status(id, user_id, status)
    if response == 200:
        return True
    return False
