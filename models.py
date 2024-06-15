class Test:
    def __init__(self, topic: str, timed: bool, scoring: str, diff: str, questions: list):
        self.topic = topic
        self.timed = timed
        self.scoring = scoring
        self.diff = diff
        self.questions = questions  # Удалить последние три значения, перенести их в класс Question
        self.questioncount = len(self.questions)

    def convert_json(self):
        """Подготоваливает объект класса Test к добавлению в json-файл"""
        tempdict = dict(topic=self.topic,
                        questioncount=self.questioncount,
                        timed=self.timed,
                        scoring=self.scoring,
                        diff=self.diff,
                        questions=self.questions,
                        answers=self.answers,
                        correct=self.correct)
        return tempdict

    def __str__(self):
        return f'''Topic: {self.topic}, Count: {self.questioncount}, {self.timed}, {self.scoring},
{self.diff}, {self.questions}, {self.answers}, {self.correct}'''


class Question:
    """Заготовка под класс, содержит текст вопроса, список вариантов ответа и номер правильного ответа"""
    def __init__(self, body: str, answers, correct=None):
        self.body = body
        self.answers = answers
        self.correct = correct

    def __repr__(self):
        return f'Question: {self.body}'

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
