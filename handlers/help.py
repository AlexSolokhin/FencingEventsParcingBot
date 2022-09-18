from loader import bot
from telebot.types import Message


@bot.message_handler(commands=['help'])
def help_command(message: Message) -> None:
    """
    Функция справка (команда /help)

    :param message: Объект сообщения.
    :type message: Message
    :return: None
    """
    bot.send_message(message.chat.id, "Вот, что я умею:\n"
                                      "\n"
                                      "/tournaments: покажу список основных предстоящих HEMA-турниров\n"
                                      "/donate: поддержать разработчиков"
                                      "/help: повторный вывод справки по командам")
