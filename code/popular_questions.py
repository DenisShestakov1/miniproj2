import sqlite3
from config import DB_PATH

def get_popular_questions():
    """Получение трёх популярных вопросов из базы данных."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Пример: запрос для получения первых трёх вопросов
    query = """
    SELECT question
    FROM questions
    ORDER BY id DESC
    LIMIT 3
    """
    
    cursor.execute(query)
    questions = [row[0] for row in cursor.fetchall()]
    conn.close()
    
    # Если нет вопросов в базе, возвращаем пустой список
    return questions or ["Вопросы пока не добавлены."]
