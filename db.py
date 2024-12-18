import sqlite3
from config import DB_PATH

def init_db():
    """Инициализация базы данных."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Создание таблиц
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fio TEXT,
        phone TEXT,
        email TEXT,
        region TEXT,
        purchase_method TEXT
    )""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fio TEXT,
        phone TEXT,
        email TEXT,
        inn TEXT
    )""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS accounting (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fio TEXT,
        phone TEXT,
        email TEXT,
        inn TEXT,
        edo TEXT
    )""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS suppliers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fio TEXT,
        phone TEXT,
        email TEXT,
        inn TEXT,
        message TEXT
    )""")

    conn.commit()
    conn.close()

def insert_data(table, data):
    """Вставка данных в таблицу."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Отладочное сообщение: проверка данных
    print(f"Попытка вставить данные в таблицу {table}: {data}")

    try:
        # Создание запроса на вставку данных с правильными placeholders
        placeholders = ", ".join(["?"] * len(data))  # Создание плейсхолдеров
        query = f"INSERT INTO {table} ({', '.join(data.keys())}) VALUES ({placeholders})"
        
        # Вставка данных
        cursor.execute(query, tuple(data.values()))

        # Подтверждение изменений
        conn.commit()
    except Exception as e:
        print(f"Ошибка при вставке данных в таблицу {table}: {e}")  # Отладочное сообщение
    finally:
        conn.close()
