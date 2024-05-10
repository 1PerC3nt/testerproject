from models import Test
from tests import tester


def show_test(item: Test):
    """Примитивный консольный интерфейс для демонстрации теста. Получает уже собранный объект класса Test,
     собирает ответы от пользователя и возвращает их в виде списка"""
    guess = []
    print(f'Starting test {item.topic}...')
    for num, i in enumerate(item.questions):
        print(f'Question: {i}')
        print(f'Possible answers: {item.answers[num]}')
        guess.append(int(input('Choose the correct answer: ')) - 1)
    print(guess)


show_test(tester)


