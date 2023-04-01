from aiogram import types

from methods.config import help_text
from keyboards.default import get_menu
from loader import dp, bot
from utils.generate_image import generate_dashboard

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    tg_id = message.from_user.id
    await message.answer("<b>Доброго времени суток!</b>", reply_markup=get_menu(tg_id))


@dp.message_handler(commands=['help'])
async def send_help_text(message: types.Message):
    tg_id = message.from_user.id
    await message.answer(help_text, reply_markup=get_menu(tg_id))


async def _analyze_product(message: types.Message):
    tg_id = message.from_user.id
    product = 'd'
    prices = [100, 50, 56, 45, 96, 90, 34, 34, 50, 100]
    sales = [100, 50, 56, 45, 96, 90, 34, 34, 50, 100]
    image = generate_dashboard(prices, sales) # TODO: сделать генерацию дашборда and model
    await bot.send_photo(tg_id, image,
                         caption=f"<b>Анализ категории '{product}' по запросу '{message.text}'</b>",
                         )


@dp.message_handler(chat_type=[types.ChatType.PRIVATE])
async def bot_message(message: types.Message):
    match message.text:
        case 'Анализировать товар':
            await _analyze_product(message)
        case 'Профиль':
            await message.answer('Ваша статистика доступна по ссылке: ')
        case _:
            await message.answer("Команда не распознана")


