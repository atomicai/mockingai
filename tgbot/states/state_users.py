from aiogram.dispatcher.filters.state import State, StatesGroup


class UserState(StatesGroup):
    inn = State()
    word = State()

