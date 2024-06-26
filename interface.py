from models import Test
from controllers import adder_controller, username_validation, admin_validation, show_controller


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


def test_adder():
    """Ручной сборщик тестов, по очереди принимает от пользователя значения полей и собирает объект класса,
     после чего добавляет его в базу. Использует примитивную валидацию получаемых данных через integrity_check.
      Ввод ответов пока поддерживает только строки"""
    print('Initialized test adder mode')
    flags = {'topic': input('Insert test topic'),
             'questioncount': int(input('Insert test question count')),
             'timed': bool(int(input('1 if timed, 0 if not'))),
             'scoring': input('Insert scoring system'),
             'diff': input('Insert test difficulty'),
             'questions': [],
             'answers': [],
             'correct': []}
    for i in range(flags['questioncount']):
        flags['questions'].append(input(f'Insert question {i + 1}'))
        flags['answers'].append([])
        while True:
            print('Insert answer, 000 if no more answers')
            answer = input()
            if answer == '000':
                break
            flags['answers'][i].append(answer)
        flags['correct'].append(input('Insert correct answer'))
    result = Test(flags['topic'],
                  flags['questioncount'],
                  flags['timed'],
                  flags['scoring'],
                  flags['diff'],
                  flags['questions'],
                  flags['answers'],
                  flags['correct'])
    return result


def entry():
    """Точка входа, она же базовая форма логина. После получения валидного имени пользователя открывает интерфейс."""
    username = input('Test platform booted up. Please enter your username to proceed')
    if username_validation(username):
        user_interface()


def user_interface():
    """Пользовательский интерфейс. Возможно в перспективе разделить админку и интерфейс юзера,
     чтобы юзер админские опции вообще не видел."""
    while True:
        mode = int(input('Input 1 to choose a test, 2 to add a test(admin), 3 to exit'))
        if mode == 1:
            testid = input('Enter test ID')  # заменить технический айдишник на более "умный" интерфейс выбора тестов
            show_test(show_controller(testid))
        if mode == 2 and admin_validation():
            adder_controller(test_adder())
        if mode == 3:
            break


if __name__ == '__main__':
    entry()
