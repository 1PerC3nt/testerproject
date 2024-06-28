class Test:
    def __init__(self, topic: str, timed: bool, scoring: str, diff: str, questions: list):
        self.topic = topic
        self.timed = timed
        self.scoring = scoring
        self.diff = diff
        self.questions = questions  # Удалить последние три значения, перенести их в класс Question
        self.questioncount = 0

    def get_correct(self):
        result = []
        for question in self.questions:
            result.append(question.correct)
        return result

    def __str__(self):
        return f'''Topic: {self.topic}, Count: {self.questioncount}, Timed: {self.timed}, Scoring: {self.scoring},
Test diff: {self.diff}, Questions: {self.questions}'''


class Question:
    """Заготовка под класс, содержит текст вопроса, список вариантов ответа и номер правильного ответа"""
    def __init__(self, body: str, answers=None, correct=None):
        if answers is None:
            answers = []
        self.body = body
        self.answers = answers
        self.correct = correct

    def __repr__(self):
        return f'Question: {self.body}, answers: {self.answers}'

    def __eq__(self, other):
        return self.body == other.body


class Answer:
    """Заготовка под класс, содержит только текст ответа"""
    def __init__(self, body: str):
        self.body = body

    def __repr__(self):
        return self.body


class User:
    def __init__(self, name, userid, isadmin):
        self.name = name
        self.userid = userid
        self.isadmin = isadmin

    def __str__(self):
        return f'User {self.name} ID: {self.userid}, Admin: {self.isadmin}'
