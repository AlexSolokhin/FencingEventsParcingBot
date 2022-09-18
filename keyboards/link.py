from telebot import types


def link_keyboard(link: str) -> types.InlineKeyboardMarkup:
    """
    Создаёт клавиатуру с ссылкой для перехода в группу турнира.

    :return: keyboard
    :rtype: InlineKeyboardMarkup
    """

    keyboard = types.InlineKeyboardMarkup()

    link = types.InlineKeyboardButton(text='Ссылка на страницу турнира', url=link)

    keyboard.add(link)

    return keyboard
