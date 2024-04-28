from models import Test
import json
import os

DATA_LOCATION = 'teststorage.json'
testid = 0 # placeholder, should generate ids somewhere


def pull(num):
    """Достает тест из файла. Все тесты хранятся в одном файле формата json,
     доступ к тестам возможен по уникальному id (нереализовано)
     НЕ РАБОТАЕТ, ПЕРЕПИСАТЬ ПОД JSON"""
    result = []
    with open(DATA_LOCATION, 'r', encoding='utf-8') as f:
        templates = json.load(f)
        return templates[num]


def adder_json(item: Test):
    """Добавляет объект Test в файл. Должна еще генерировать айдишник для записываемого теста,
     но я пока не разобрался, как это сделать"""
    with open(DATA_LOCATION, 'a', encoding='utf-8') as f:
        json.dump(item.convert_json(testid), f)


def debugmode():
    while True:
        print('0 to add, 1 to read, 2 to clear, 3 to create, 4 to delete, 5 to exit')
        mode = int(input())
        if mode == 0:
            adder_json(tester)
        elif mode == 1:
            try:
                temp = pull('0')
                print(temp)
            except Exception:
                print('error')
        elif mode == 2:
            with open(DATA_LOCATION, 'w', encoding='utf-8') as f:
                f.write('')
        elif mode == 3:
            with open(DATA_LOCATION, 'w', encoding='utf-8') as f:
                pass
        elif mode == 4:
            os.remove(DATA_LOCATION)
        elif mode == 5:
            break


tester = Test('Math',
              5,
              False,
              'basic',
              'easy',
              ['a', 'b', 'c'],
              [['a', 'b'], [1, 2], [True, False]],
              ['a', 2, False])
if __name__ == '__main__':
    debugmode()
