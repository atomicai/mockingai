from aiogram import types

from tgbot.methods.config import help_text
from tgbot.keyboards.default import get_menu
from tgbot.keyboards.inline import select_category
from tgbot.loader import dp, bot
from tgbot.utils.generate_image import generate_dashboard


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    tg_id = message.from_user.id
    await message.answer("<b>Привет! Я бот, который поможет тебе анализировать категории на рентабельность. "
                         "Просто отправь мне список твоих категорий и я помогу тебе определить, "
                         "какие из них приносят наибольшую прибыль, а какие нуждаются в улучшении. "
                         "Я был создан, чтобы сделать твой бизнес более прибыльным и эффективным. "
                         "Начнем работу!</b>", reply_markup=get_menu(tg_id))


@dp.message_handler(commands=['help'])
async def send_help_text(message: types.Message):
    tg_id = message.from_user.id
    await message.answer(help_text, reply_markup=get_menu(tg_id))


@dp.callback_query_handler(text_contains="#")
async def process_callback(callback_query: types.CallbackQuery):
    tg_id = callback_query.message.chat.id
    product = str(callback_query.data)[1:]
    prices = [100, 50, 56, 45, 96, 90, 34, 34, 50, 100]
    sales = [1000, 500, 400, 450, 960, 900, 340, 340, 200, 1000]  # TODO: model
    image = generate_dashboard(prices, sales)
    await bot.send_photo(tg_id, image,
                         caption=f'<b>Анализ категории "{product}"</b>', )


async def _analyze_product(message: types.Message):
    products = {"Ремонт", "Электроника", 'Бла бла'}
    await message.answer('Выберите категорию товара', reply_markup=select_category(products))


@dp.message_handler(chat_type=[types.ChatType.PRIVATE])
async def bot_message(message: types.Message):
    match message.text:
        case 'Анализировать товар':
            await _analyze_product(message)
        case 'Профиль':
            await message.answer('Ваша статистика доступна по ссылке: ')
        case _:
            await message.answer("Команда не распознана")


