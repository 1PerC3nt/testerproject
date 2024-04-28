from models import Test
import json
import os

DATA_LOCATION = 'teststorage.json'


def pull(num):
    """Достает тест из файла. Все тесты хранятся в одном файле формата json,
     доступ к тестам возможен по уникальному id (нереализовано)"""
    result = []
    with open(DATA_LOCATION, 'r', encoding='utf-8') as f:
        templates = json.load(f)
        testobj = Test(templates[num]['topic'],
                       templates[num]['questioncount'],
                       templates[num]['timed'],
                       templates[num]['scoring'],
                       templates[num]['diff'],
                       templates[num]['questions'],
                       templates[num]['answers'],
                       templates[num]['correct'])
        return testobj


def adder_json(item: Test, testid):
    """Добавляет объект Test в файл. Должна еще генерировать айдишник для записываемого теста,
     но я пока не разобрался, как это сделать"""
    with open(DATA_LOCATION, 'r', encoding='utf-8') as f:
        try:
            items = json.load(f)
        except Exception:
            items = {}
    with open(DATA_LOCATION, 'w', encoding='utf-8') as f:
        items[testid] = item.convert_json()
        json.dump(items, f, indent=3)


def debugmode():
    """Простой инструмент для тестирования функций, позволяет вручную добавлять, читать или удалять тесты,
     а также удалять и пересоздавать файл с базой, если все сломалось"""
    while True:
        print('0 to add, 1 to read, 2 to clear, 3 to create, 4 to delete, 5 to exit')
        mode = int(input())
        if mode == 0:
            testid = int(input('ID placeholder'))
            adder_json(tester, testid)
        elif mode == 1:
            try:
                testid = input('ID placeholder')
                temp = pull(testid)
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
              ['amogus?', 'bingus?', 'the cake is a lie?'],
              [['yeah', 'nah'], [1, 2], [True, False]],
              ['yeah', 2, False])
