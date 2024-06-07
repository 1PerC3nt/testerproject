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

    def pull(self, num):
        """Достает тест из базы. Из-за структуры БД поочередно делает несколько запросов и раскладывает
         полученные данные по переменным, после чего формирует из них объект класса Test.
          Очень громоздкое из-за необходимости вручную распределять данные 'по полочкам'."""
        query = f'''
        select * from Tests where test_id = {num};
        '''
        cursor = self.connection.execute(query)
        testdata = cursor.fetchall()
        query = f'''
        select * from Questions where test_id = {num};
        '''
        cursor = self.connection.execute(query)
        questiondata = cursor.fetchall()
        questions = []
        correct = []
        for i in questiondata:  # Разносим данные о вопросах по двум спискам для дальнейшего формирования объекта
            questions.append(i[1])
            correct.append(i[2])
        variantdata = []
        for i in range(1, len(questiondata)+1):  # Возможно ли достать все варианты ответа одним sql-запросом?
            query = f'''
            select body from Variants where question_id = {i}
            '''
            cursor = self.connection.execute(query)
            variantdata.append(cursor.fetchall())
        testobj = Test(
            topic=testdata[0][1],
            questioncount=len(questiondata),
            timed=False,  # пока всегда False
            scoring=testdata[0][2],
            diff='Placeholder',  # пока не хранится в БД, возможно лишний параметр
            questions=questions,
            answers=variantdata,
            correct=correct
        )
        return testobj

    def adder_sql(self, item: Test, testid):
        """Добавляет объект класса Test в БД. Скорее всего, нужна транзакция,
         чтобы гарантировать занесение целостного теста,
          тк он хранится по разным таблицам и нужно будет сделать несколько операций.
           Она же заменит старый метод integrity_check, использовавшийся для тех же целей."""
        pass

