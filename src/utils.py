from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def lets_start_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='Давай начнём!')]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )

    return keyboard


def gender_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='Я девушка'),
             KeyboardButton(text='Я парень')]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )

    return keyboard


def no_desc_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='Не хочу заполнять информацию о себе')]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )

    return keyboard
