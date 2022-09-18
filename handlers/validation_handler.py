from loader import bot
import json
from telebot.types import CallbackQuery
from keyboards.link import link_keyboard


@bot.callback_query_handler(func=lambda call: True)
def tournaments_validation_handler(callback: CallbackQuery) -> None:
    """
    По решению админа, добавляет турнир в БД или игнорит его

    :param callback: Объект CallBackQuery
    :type: CallbackQuery
    :return: None
    """

    callback_json = json.loads(callback.data)
    decision = callback_json['method']
    link = callback_json['link']

    if decision == 'ADD':
        # add_to_db(link) - функция для добавления в БД
        bot.send_message(callback.message.chat.id, f'Турнир по ссылке {link} добавлен в базу данных')

    elif decision == 'IGNORE':
        pass
        # Пока просто оставил конструкцию. Если парсер будет слать много мусора, можно будет сделать ЧС и слать туда.

    bot.delete_message(callback.message.chat.id, callback.message.id)
