import time

import telebot

import config as cfg
from api_dostavka import send_confirmation_request, get_last_orders
from text import format_orders_summary
from utils import generate_inline_keyboard, generate_final_inline_keyboard, change_status

bot = telebot.TeleBot(cfg.BOT_TOKEN)


@bot.message_handler(commands=['start'])
def handle_start(message):
    text = message.text
    if len(text.split()) > 1:
        start_param = text.split()[1]
        response = send_confirmation_request(start_param, str(message.from_user.id))
        if response:
            bot.reply_to(message, f'Вы успешно авторизированы в системе!', parse_mode='Markdown',
                         reply_markup=generate_inline_keyboard())
        else:
            bot.reply_to(message, f'Ошибка на стороне сервиса!', parse_mode='Markdown')
    else:
        bot.reply_to(message, 'Ошибка авторизации, попробкйте снова!', parse_mode='Markdown')


@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    if call.data == "approved":
        response = change_status(call.message.text, call.message.chat.id, "approved")
        if response:
            keyboard = generate_final_inline_keyboard()
            bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          reply_markup=keyboard)
    elif call.data == "closed":
        response = change_status(call.message.text, call.message.chat.id, "closed")
        if response:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Отменено\n" + call.message.text, reply_markup=None)
    elif call.data == "completed":
        response = change_status(call.message.text, call.message.chat.id, "completed")
        if response:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Выполнено\n" + call.message.text, reply_markup=None)


@bot.message_handler(func=lambda message: message.text == "Мои заказы")
def handle_my_orders(message):
    response = get_last_orders(message.from_user.id)
    response_message = format_orders_summary(response)
    bot.send_message(message.chat.id, response_message)


if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            print(f"Error occurred: {e}")
            time.sleep(1)
