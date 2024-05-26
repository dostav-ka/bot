from flask import Blueprint, request, jsonify

from api_utils import generate_inline_keyboard
from texts import format_new_order_message


class MessageBlueprint(Blueprint):
    def __init__(self, bot, cfg):
        super(MessageBlueprint, self).__init__("message", __name__)
        self.bot = bot
        self.cfg = cfg
        self._register_routes()

    def _register_routes(self):
        self.add_url_rule(
            view_func=self.send_request,
            rule="/request",
            methods=["POST"]
        )

    def send_request(self):
        data = request.json
        telegram_id = data.get('tg_id')
        message = format_new_order_message(data)
        keyboard = generate_inline_keyboard()
        self.bot.send_message(telegram_id, message, reply_markup=keyboard)

        return jsonify({"message": "OK"})
