from aiogram import executor
import middlewares
from handlers import dp
from utils import set_bot_commands


async def on_startup(dp):
    middlewares.setup(dp)
    await set_bot_commands.set_default_commands(dp)
    print("Бот успешно запущен")


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup)