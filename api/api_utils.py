from telebot import types


def generate_inline_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    accept_button = types.InlineKeyboardButton(text="Принять", callback_data="approved")
    decline_button = types.InlineKeyboardButton(text="Отказать", callback_data="closed")
    keyboard.add(accept_button, decline_button)
    return keyboard
