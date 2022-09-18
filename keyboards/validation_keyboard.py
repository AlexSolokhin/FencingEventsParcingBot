from telebot import types


def validation_keyboard(link) -> types.InlineKeyboardMarkup:
    """
    Создаёт клавиатуру для валидации найденных турниров админом.

    :return: keyboard
    :rtype: InlineKeyboardMarkup
    """

    keyboard = types.InlineKeyboardMarkup()

    add = types.InlineKeyboardButton(text='Это подходит', callback_data='{method: ADD, link: ' + link + '}')
    ignore = types.InlineKeyboardButton(text='Это не то', callback_data='{method: IGNORE, link: ' + link + '}')

    keyboard.add(add)
    keyboard.add(ignore)

    return keyboard
