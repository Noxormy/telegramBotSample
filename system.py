import telebot
from db import db
from localization import localization
from logger import add_handler
from wrappers import for_users_with_data

API_KEY = "1947801017:AAG74HbSm_JFexjldoGagt0GJCncLJoMrds"
bot = telebot.TeleBot(API_KEY, parse_mode=None)


default_user_data = {
    u"locale": "en"
}
users = db.collection(u"users")


class System:
    LOCALE = u"locale"
    LOG_CHAT = 0

    def __init__(self):
        if System.LOG_CHAT != 0:
            add_handler(lambda msg: bot.send_message(System.LOG_CHAT, msg))

        self.__init_localization()
        self.admins = [0]

    @for_users_with_data(users, default_user_data)
    def set_locale_for_user(self, doc_ref, chat_id, locale):
        doc_ref.update({System.LOCALE: locale})

    @for_users_with_data(users, default_user_data)
    def get_user_locale(self, doc_ref, chat_id):
        doc = doc_ref.get()
        data = doc.to_dict()

        return data[System.LOCALE]

    def __init_localization(self):
        localization.set_locales_directory('./locales')
        localization.set_locale('ru')


system = System()
