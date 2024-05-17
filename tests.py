from repository import adder_json, pull, DATA_LOCATION, Test
from interface import test_adder
import os


def debugmode():
    """Простой инструмент для тестирования функций, позволяет вручную добавлять, читать или удалять тесты,
     а также удалять и пересоздавать файл с базой, если все сломалось"""
    while True:
        print('0 to add, 1 to read, 2 to clear, 3 to create, 4 to delete, 5 to add test(manual), 6 to exit')
        mode = int(input())
        if mode == 0:
            testid = int(input('ID placeholder'))
            adder_json(testdata1, testid)
        elif mode == 1:
            try:
                testid = input('ID placeholder')
                temp = pull(testid)
                print(temp)
            except ValueError:
                print('Integrity check not passed')
        elif mode == 2:
            with open(DATA_LOCATION, 'w', encoding='utf-8') as f:
                f.write('')
        elif mode == 3:
            with open(DATA_LOCATION, 'w', encoding='utf-8') as f:
                pass
        elif mode == 4:
            os.remove(DATA_LOCATION)
        elif mode == 5:
            test_adder()
        elif mode == 6:
            break


testdata0 = Test('Math',
                 3,
                 False,
                 'basic',
                 'easy',
                 ['amogus?', 'bingus?', 'the cake is a lie?'],
                 [['yeah', 'nah'], [1, 2], [True, False]],
                 ['yeah', 2, False])
testdata1 = Test('Physics',
                 4,
                 False,
                 'adv',
                 'medium',
                 ['sus?', '2+2?', 'arirals are real?'],
                 [['yeah', 'nah'], [1, 2, 4], [True, False]],
                 ['nah', 4, True])
if __name__ == '__main__':
    debugmode()