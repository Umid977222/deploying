from aiogram import types
from bot.get_data import buttons


def kb1():
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text="Продукция 📦")
    )
    return keyboard


def kb2():
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text="ВСТРАИВАЕМАЯ ТЕХНИКА"))
    return keyboard


def kb3():
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    keyboard.add(*buttons)
    return keyboard
