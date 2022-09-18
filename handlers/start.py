from loader import bot
from telebot.types import Message


@bot.message_handler(commands=['start'])
def greetings(message: Message) -> None:
    """
    Функция-приветствие (команда start)

    :param message: Объект сообщения.
    :type message: Message
    :return: None
    """
    bot.send_message(message.chat.id, 'Привет!\n'
                                      'Меня разработали ребята из Нижегородского клуба СКИФ.\n'
                                      'С моей помощью ты узнаешь об основных предстоящих HEMA-турнирах.\n'
                                      'Чтобы начать, используй команду /tournaments')
