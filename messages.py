from localization import _
from system import bot, system


@bot.message_handler(commands=['start'])
def start_handler(message):
    chat_id = message.chat.id
    locale = system.get_user_locale(chat_id)
    bot.send_message(chat_id, _('start_response', locale))


@bot.message_handler(commands=['set_locale'])
def start_handler(message):
    chat_id = message.chat.id

    text = message.text.split()
    if len(text) == 2:
        locale = text[1]
        system.set_locale_for_user(chat_id, locale)
        bot.send_message(chat_id, _('locale_changed', locale))
    else:
        locale = system.get_user_locale(chat_id)
        bot.send_message(chat_id, _('locale_change_error', locale))
