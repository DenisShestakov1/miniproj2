import unittest
from handlers import handle_user_input
from ui import render_question_list
from db import insert_question, fetch_all_questions
from cleaning import clean_text
from config import load_config

class TestHandlers(unittest.TestCase):
    def test_handle_user_input_valid(self):
        """Тест: Проверка обработки валидного пользовательского ввода."""
        result = handle_user_input("What is AI?")
        self.assertEqual(result, {"status": "success", "message": "Input processed"})

class TestUI(unittest.TestCase):
    def test_render_question_list(self):
        """Тест: Проверка рендера списка вопросов."""
        questions = ["What is AI?", "What is Python?"]
        result = render_question_list(questions)
        self.assertIn("What is AI?", result)
        self.assertIn("What is Python?", result)

class TestDB(unittest.TestCase):
    def test_insert_question(self):
        """Тест: Проверка вставки вопроса в базу данных."""
        question = {"id": 1, "text": "What is AI?", "popularity": 100}
        result = insert_question(question)
        self.assertTrue(result)

    def test_fetch_all_questions(self):
        """Тест: Проверка выборки всех вопросов из базы данных."""
        result = fetch_all_questions()
        self.assertIsInstance(result, list)

class TestCleaning(unittest.TestCase):
    def test_clean_text_removes_special_characters(self):
        """Тест: Проверка очистки текста от специальных символов."""
        dirty_text = "What is AI?!@#$"
        result = clean_text(dirty_text)
        self.assertEqual(result, "What is AI")

class TestConfig(unittest.TestCase):
    def test_load_config_valid_file(self):
        """Тест: Проверка загрузки конфигурации из валидного файла."""
        config_path = "config.json"
        result = load_config(config_path)
        self.assertIn("database_url", result)

if __name__ == "__main__":
    unittest.main()
