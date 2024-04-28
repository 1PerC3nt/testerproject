from models import Test
import json
DATA_LOCATION = 'teststorage.json'


def pull(num):
    """Достает тест из файла. Все тесты хранятся в одном файле формата json,
     доступ к тестам возможен по уникальному id (нереализовано)
     НЕ РАБОТАЕТ, ПЕРЕПИСАТЬ ПОД JSON"""
    result = []
    with open(DATA_LOCATION, 'r', encoding='utf-8') as f:
        for i in f.readlines():
            if i == 'Splitter\n':
                num -= 1
                continue
            if num == 1:
                result.append(i.strip())
        return result


def adder_json(item: Test):
    """Добавляет объект Test в файл. Должна еще генерировать айдишник для записываемого теста,
     но я пока не разобрался, как это сделать"""
    with open(DATA_LOCATION, 'a', encoding='utf-8') as f:
        f.write(item.convert_json(len(DATA_LOCATION)))


temp = pull(2)
print(temp)
tester = Test('Math',
              5,
              False,
              'basic',
              'easy',
              ['a', 'b', 'c'],
              [['a', 'b'], [1, 2], [True, False]],
              ['a', 2, False])
adder_json(tester)
