from models import Test, Question, User
import sqlite3
from pathlib import Path

DATA_LOCATION = Path(__file__) / Path('./storage/storage.db').resolve()


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
            questions=[Question(data[0][3], None, data[0][4])],
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

    def get_user(self, username):
        """Получает данные о пользователе из БД."""
        query = f'''
        select * from Users
        where username =?;
        '''
        cursor = self.connection.execute(query, (username,))
        data = cursor.fetchall()[0]
        user = User(data[1], data[0], bool(data[2]))
        return user

    def add_answers(self, question_id: int, answers: list):
        """Добавляет список ответов в БД."""
        for answer in answers:
            query = '''
            insert into Variants(body, question_id)
            values(?, ?);
            '''
            self.connection.execute(query, [answer, question_id])
            self.connection.commit()

    def add_questions(self, test_id: int, questions: list):
        """Добавляет список объектов класса Question в БД."""
        for question in questions:
            query = '''
            insert into Questions(title, answer, test_id)
            values(?, ?, ?) returning question_id;
            '''
            cursor = self.connection.execute(query, [question.body, question.correct, test_id])
            question_id = cursor.fetchone()
            self.connection.commit()
            self.add_answers(question_id[0], question.answers)

    def add_test(self, item: Test):
        """Добавляет объект класса Test в БД."""
        try:
            query = '''
            insert into Tests(theme, scoringSystem)
            values(?, ?) returning test_id;
            '''
            cursor = self.connection.execute(query, [item.topic, item.scoring])
            test_id = cursor.fetchone()
            self.connection.commit()
            self.add_questions(test_id[0], item.questions)
        except sqlite3.Error:
            print('Adder failed')
            self.connection.rollback()  # Не откатывает изменения в базе при провале транзакции

    def add_result(self, score: int, user_id, test_id):
        """Добавляет информацию о результатах пройденного теста в БД."""
        query = '''
        insert into Results(test_id, user_id, score)
        values(?, ?, ?);
        '''
        self.connection.execute(query, [test_id, user_id, score])
        self.connection.commit()
