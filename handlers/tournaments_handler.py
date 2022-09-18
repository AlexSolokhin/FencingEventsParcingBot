from loader import bot
from telebot.types import Message
from keyboards.link import link_keyboard


@bot.message_handler(commands=['tournaments'])
def show_tournaments_handler(message: Message) -> None:
    """
    Функция справка (команда /help)

    :param message: Объект сообщения.
    :type message: Message
    :return: None
    """

    # tournaments_list = get_tournaments() - функция, которая забирает из БД будущие турниры. Возвращает list или tuple
    # Список/кортеж должен содержать словари с основной информацией по турнирам
    tournaments_list = []
    # Пока делаю пустой список

    for tournament in tournaments_list:
        name = tournament['name']
        date = tournament['date']
        place = tournament['place']
        nominations = tournament['nominations']
        link = tournament['link']
        description = tournament['description']
        # Подправим параметры сообщения в зависимости от того, что сможем спарсить.

        message_text = f'{name}\n\n' \
                       f'Дата проведения: {date}\n' \
                       f'Место проведения: {place}\n' \
                       f'Номинации: {nominations}\n\n' \
                       f'{description}'

        bot.send_message(message.chat.id, message_text, reply_markup=link_keyboard(link))
