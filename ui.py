from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_main_menu():
    """Главное меню."""
    menu = ReplyKeyboardMarkup(resize_keyboard=True)
    menu.add(KeyboardButton("🎁Оформить Заказ🎁"))
    menu.add(KeyboardButton("⁉️Вопросы по действующему заказу⁉️"))
    menu.add(KeyboardButton("📜✍️Бухгалтерские документы📜✍️"))
    menu.add(KeyboardButton("🚚Стать нашим Поставщиком🚚"))
    return menu

def get_questions_menu():
    """Меню для раздела 'Вопросы по заказу'."""
    menu = ReplyKeyboardMarkup(resize_keyboard=True)
    menu.add(KeyboardButton("Самые популярные вопросы"))
    menu.add(KeyboardButton("Назад"))
    return menu
