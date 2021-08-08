import functools
import telebot

from localization import localization
from logger import logger, add_handler

API_KEY = "1917406526:AAERd_pOLx5aF4AAyBlINTgajNtSD_-1_QI"
bot = telebot.TeleBot(API_KEY, parse_mode=None)


def admins_only(func):
    """
        There should be chat_id in wrapped function arguments
    """
    @functools.wraps(func)
    def wrapped_func(self, *args, **kwargs):
        chat_id = kwargs.get("chat_id")
        if chat_id in self.admins:
            return func(self, *args, **kwargs)
        else:
            logger.info(
                "You can't use function [{}] without admin rights, chat_id: [{}]".format(func.__name__, chat_id))
            return False

    return wrapped_func


class System:
    LOCALE = "locale"

    def __init__(self):
        log_chat = 0
        if log_chat != 0:
            add_handler(lambda msg: bot.send_message(log_chat, msg))

        self.admins = [0]
        self.users_settings = {}

    def set_locale_for_user(self, chat_id, locale="en"):
        self.users_settings[chat_id] = {
            System.LOCALE: locale
        }

    def get_user_locale(self, chat_id):
        if not (chat_id in self.users_settings.keys()) or not (System.LOCALE in self.users_settings[chat_id]):
            self.set_locale_for_user(chat_id)

        return self.users_settings[chat_id].get(System.LOCALE)


system = System()
localization.set_locales_directory('./locales')
localization.set_locale('ru')
