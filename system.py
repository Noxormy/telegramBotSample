import telebot
from logger import logger, add_handler

API_KEY = 'API_KEY'
bot = telebot.TeleBot(API_KEY, parse_mode=None)


class System:
    def __init__(self):
        log_chat = 00000
        add_handler(lambda msg: bot.send_message(log_chat, msg))

        self.admins = []


system = System()
