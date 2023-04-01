from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo


def select_category(categories: dict):
    keyboard = InlineKeyboardMarkup(row_width=1)

    for category in categories:
        button = InlineKeyboardButton(text=category, callback_data=f"#{category}")
        keyboard.add(button)
    return keyboard
