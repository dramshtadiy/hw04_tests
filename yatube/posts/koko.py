def movie_quotes(name):
    """Возвращает цитаты известных персонажей из фильмов."""
    quotes = {
        'Алиса Плезенс Лидделл': 'Всё чудесатее и чудесатее!',
        'Элли': 'Тото , у меня такое ощущение, что мы не в Канзасе!',
        'Шерлок': 'Элементарно, Ватсон!',
        'Дарт Вейдер': 'Я — твой отец.',
        'Thomas A. Anderson': 'Меня. Зовут. Нео!',
    }
    return quotes.get(name, 'Персонаж пока не известен миллионам.')

# Утверждаем, что если в movie_quotes() передать 'Шерлок' -
# функция вернёт 'Элементарно, Ватсон!'.


assert movie_quotes('Шерлок') == 'Элементарно, Ватсон!', (
    "movie_quotes('Шерлок') не вернул ожидаемый результат!")

# Утверждаем, что если в movie_quotes() передать 'Thomas A. Anderson' -
# функция вернёт 'Меня зовут Нео!'.
assert movie_quotes('Thomas A. Anderson') == 'Меня. Зовут. Нео!', (
    "movie_quotes('Thomas A. Anderson') не вернул ожидаемый результат!")

# Утверждаем, что если в movie_quotes передать 'Алиса Плезенс Лидделл' -
# функция вернёт 'Всё чудесатее и чудесатее!'.
expected_answer = 'Всё чудесатее и чудесатее!'
assert movie_quotes('Алиса Плезенс Лидделл') == expected_answer, (
    "movie_quotes('Алиса Плезенс Лидделл') не вернул ожидаемый результат!")
