class Test:
    def __init__(self, topic: str, questioncount: int, timed: bool, scoring: str, diff: str, questions: list, answers: list, correct: str):
        self.topic = topic
        self.questioncount = questioncount
        self.timed = timed
        self.scoring = scoring
        self.diff = diff
        self.questions = questions
        self.answers = answers
        self.correct = correct


class User:
    def __init__(self, name, userid, isadmin):
        self.name = name
        self.userid = userid
        self.isadmin = isadmin


