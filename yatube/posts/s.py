import unittest
def ultimate_answer(question):
    """Выводит на печать переданный аргумент и возвращает строку ответа."""
    print(f'Ваш вопрос: {question}')
    return f'Ответ на ваш вопрос "{question}": 42' 
def test_case_1(self):
    self.assertIsInstance(ultimate_answer('Что делать?'), str, 'Тест провален')