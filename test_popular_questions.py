import pytest
import sqlite3
from popular_questions import get_popular_questions

# Укажите путь к тестовой базе данных
TEST_DB_PATH = "questions.db"

@pytest.fixture
def setup_test_db():
    """Создание тестовой базы данных перед тестами."""
    conn = sqlite3.connect(TEST_DB_PATH)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS questions (id INTEGER PRIMARY KEY, question TEXT)")
    conn.commit()
    yield conn  # Передаём соединение в тест
    conn.close()

def test_get_popular_questions(setup_test_db, monkeypatch):
    """Тестируем функцию получения популярных вопросов."""
    # Подменяем путь к базе данных
    monkeypatch.setattr('popular_questions.DB_PATH', TEST_DB_PATH)

    # Добавляем данные в базу
    cursor = setup_test_db.cursor()
    cursor.execute("INSERT INTO questions (question) VALUES ('Какой статус моего заказа?')")
    cursor.execute("INSERT INTO questions (question) VALUES ('Как изменить адрес доставки?')")
    cursor.execute("INSERT INTO questions (question) VALUES ('Сколько времени занимает доставка?')")
    setup_test_db.commit()

    # Вызываем тестируемую функцию
    questions = get_popular_questions()
    
    # Проверяем, что возвращаются три вопроса
    assert len(questions) == 3
    assert "Какой статус моего заказа?" in questions
    assert "Как изменить адрес доставки?" in questions
    assert "Сколько времени занимает доставка?" in questions

def test_empty_database(setup_test_db, monkeypatch):
    """Тестируем функцию на пустой базе данных."""
    # Подменяем путь к базе данных
    monkeypatch.setattr('popular_questions.DB_PATH', TEST_DB_PATH)

    # Вызываем тестируемую функцию
    questions = get_popular_questions()
    
    # Проверяем, что возвращается сообщение о пустых данных
    assert questions == ["Вопросы пока не добавлены."]

def test_more_than_three_questions(setup_test_db, monkeypatch):
    """Тестируем, что возвращаются не более трёх вопросов."""
    # Подменяем путь к базе данных
    monkeypatch.setattr('popular_questions.DB_PATH', TEST_DB_PATH)

    # Добавляем более трёх вопросов в базу
    cursor = setup_test_db.cursor()
    cursor.execute("INSERT INTO questions (question) VALUES ('Вопрос 1')")
    cursor.execute("INSERT INTO questions (question) VALUES ('Вопрос 2')")
    cursor.execute("INSERT INTO questions (question) VALUES ('Вопрос 3')")
    cursor.execute("INSERT INTO questions (question) VALUES ('Вопрос 4')")
    setup_test_db.commit()

    # Вызываем тестируемую функцию
    questions = get_popular_questions()
    
    # Проверяем, что возвращаются ровно три вопроса
    assert len(questions) == 3
    assert "Вопрос 4" in questions  # Последний добавленный вопрос должен быть первым в выдаче
    assert "Вопрос 3" in questions
    assert "Вопрос 2" in questions
    assert "Вопрос 1" not in questions  # Самый старый вопрос не должен вернуться
