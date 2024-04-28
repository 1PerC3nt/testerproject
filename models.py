import json


class Test:
    def __init__(self, topic: str, questioncount: int, timed: bool, scoring: str, diff: str, questions: list,
                 answers: list, correct: list):
        self.topic = topic
        self.questioncount = questioncount
        self.timed = timed
        self.scoring = scoring
        self.diff = diff
        self.questions = questions
        self.answers = answers
        self.correct = correct

    def convert_json(self, testid):
        """Подготоваливает объект класса Test к добавлению в json-файл"""
        tempdict = dict(topic=self.topic,
                        questioncount=self.questioncount,
                        timed=self.timed,
                        scoring=self.scoring,
                        diff=self.diff,
                        questions=self.questions,
                        answers=self.answers,
                        correct=self.correct)
        resultdict = {testid: tempdict}
        return json.dumps(resultdict)


class User:
    def __init__(self, name, userid, isadmin):
        self.name = name
        self.userid = userid
        self.isadmin = isadmin
