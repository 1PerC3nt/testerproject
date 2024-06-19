from models import Test, Question
import sqlite3
from pathlib import Path

DATA_LOCATION = Path('./storage/storage.db')


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

        test = Test(
            topic=data[0][1],
            timed=False,  # пока всегда False
            scoring=data[0][2],
            diff='Placeholder',  # пока не хранится в БД, возможно лишний параметр
            questions=[Question(data[0][3])],  # впихнуть куда-то билдер объектов класса Question(возможно @classmethod)
        )
        for j in data:
            new_question = Question(j[3])

            if new_question not in test.questions:
                new_question.correct = j[4]
                new_question.answers.append(j[5])
                test.questions.append(new_question)
            else:
                test.questions[-1].answers.append(j[5])
        test.questioncount = len(test.questions)
        return test

    def adder_sql(self, item: Test, testid):
        """Добавляет объект класса Test в БД. Скорее всего, нужна транзакция,
         чтобы гарантировать занесение целостного теста,
          тк он хранится по разным таблицам и нужно будет сделать несколько операций.
           Она же заменит старый метод integrity_check, использовавшийся для тех же целей."""
        pass