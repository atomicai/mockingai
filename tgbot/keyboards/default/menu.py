from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo


def get_menu(tg_id: int):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    btn_profile = KeyboardButton('Профиль')
    btn_hw = KeyboardButton('Анализировать товар')
    keyboard.add(btn_profile, btn_hw)

    return keyboard
