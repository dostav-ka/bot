import telebot
from flask import Flask, Request
from flask_cors import CORS

import config as cfg

app = Flask(__name__)
app.config.from_object(cfg)

bot = telebot.TeleBot(cfg.BOT_TOKEN)

from message import MessageBlueprint

message_blueprint = MessageBlueprint(bot, cfg)
app.register_blueprint(message_blueprint, url_prefix="/message")

CORS(app, resources={r"/*": {"origins": "*"}})


@app.after_request
def _(r: Request) -> Request:
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'

    return r


if __name__ == "__main__":
    app.run(
        port=cfg.PORT,
        host=cfg.HOST,
        debug=cfg.DEBUG,
        use_reloader=cfg.DEBUG,
    )
