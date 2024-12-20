import sqlite3

# Создаем подключение к базе данных
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Функция для очистки таблицы
def clear_table(table_name):
    cursor.execute(f"DELETE FROM {table_name}")
    conn.commit()
    print(f"Все записи из таблицы {table_name} были удалены.")

# Очистка всех таблиц
tables = ["orders", "questions", "accounting", "suppliers"]
for table in tables:
    clear_table(table)

# Закрытие подключения
conn.close()
