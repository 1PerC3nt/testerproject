from models import Test
import sqlite3

DATA_LOCATION = '..\\storage\\storage.db'


class SqliteRepository:
    connection = None

    def __init__(self):
        self.connection = sqlite3.connect(DATA_LOCATION)

    def get_tests(self):
        query = '''
        select * from Tests;
        '''
        cursor = self.connection.execute(query)
        data = cursor.fetchall()
        print(data)

    def pull(self, test_id):
        """Достает один тест из базы. Использует всего один SQL-запрос и парсит полученные данные, заполняя словарь.
         Затем формирует объект класса Test из полученных данных (билдер возможно вынести в отдельный метод
          самого класса Test, заодно проще будет потом интегрировать модели для вопросов"""
        query = f'''
        select t.*, q.title, q.answer, v.body from Tests t
        inner join main.Questions Q on t.test_id = Q.test_id
        inner join main.Variants V on Q.question_id = V.question_id
        where t.test_id = {test_id};
        '''
        cursor = self.connection.execute(query)
        data = cursor.fetchall()
        parsed = {
            'test_id': data[0][0],
            'theme': data[0][1],
            'scoring': data[0][2],
            'questions': [data[0][3]],
            'answers': [[]],
            'correct': [data[0][4]]
        }
        temp = 0
        for i, j in enumerate(data):
            if j[3] not in parsed['questions']:
                parsed['questions'].append(j[3])
                parsed['correct'].append(j[4])
                parsed['answers'].append([])
                temp += 1
            parsed['answers'][temp].append(j[5])
        testobj = Test(
            topic=parsed['theme'],
            questioncount=len(parsed['questions']),
            timed=False,  # пока всегда False
            scoring=parsed['scoring'],
            diff='Placeholder',  # пока не хранится в БД, возможно лишний параметр
            questions=parsed['questions'],
            answers=parsed['answers'],
            correct=parsed['correct']
        )
        return testobj

    def adder_sql(self, item: Test, testid):
        """Добавляет объект класса Test в БД. Скорее всего, нужна транзакция,
         чтобы гарантировать занесение целостного теста,
          тк он хранится по разным таблицам и нужно будет сделать несколько операций.
           Она же заменит старый метод integrity_check, использовавшийся для тех же целей."""
        pass