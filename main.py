# main.py
from aiogram import Bot, Dispatcher, executor, types
from config import API_TOKEN
from handlers import handle_menu, collect_data, handle_questions_menu
from ui import get_main_menu, get_questions_menu

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Структура для хранения данных пользователей
user_data = {}

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    """Команда /start"""
    user_id = message.chat.id
    user_data[user_id] = {"step": None, "data": {}}
    await message.answer("Добро пожаловать! Выберите действие:", reply_markup=get_main_menu())

@dp.message_handler(lambda msg: msg.text in [
    "🎁Оформить Заказ🎁",
    "⁉️Вопросы по действующему заказу⁉️",
    "📜✍️Бухгалтерские документы📜✍️",
    "🚚Стать нашим Поставщиком🚚"
])
async def menu_handler(message: types.Message):
    """Обработка выбора из главного меню"""
    await handle_menu(message, user_data)

@dp.message_handler()
async def data_handler(message: types.Message):
    """Обработка данных"""
    await collect_data(message, user_data)
    
@dp.message_handler(lambda msg: msg.text == "⁉️Вопросы по действующему заказу⁉️")
async def questions_handler(message: types.Message):
    """Обработка кнопки 'Вопросы по заказу'."""
    await message.answer("Выберите действие:", reply_markup=get_questions_menu())

@dp.message_handler(lambda msg: msg.text in ["Самые популярные вопросы", "Назад"])
async def popular_questions_handler(message: types.Message):
    """Обработка кнопки 'Самые популярные вопросы'."""
    await handle_questions_menu(message)
   

if __name__ == '__main__':
    from db import init_db
    init_db()  # Инициализация базы данных
    executor.start_polling(dp, skip_updates=True)
