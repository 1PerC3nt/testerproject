from models import Test
import json


DATA_LOCATION = 'teststorage.json'


def pull(num):
    """Достает тест из файла. Все тесты хранятся в одном файле формата json,
     доступ к тестам возможен по уникальному id (нереализовано)"""
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
        if integrity_check(testobj):
            return testobj
        else:
            raise ValueError # Возможно написать кастомное исключение


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


def integrity_check(item: Test):
    """Проверяет целостность передаваемого объекта. Функция сравнивает количество вопросов с длинами соответсвующих
     списков, а также наличие правильного ответа среди представленных"""
    if len(item.answers) == len(item.correct) == len(item.questions) == item.questioncount:
        pass
    else:
        return False
    for i in range(len(item.answers)):
        if item.correct[i] not in item.answers[i]:
            return False
    return True