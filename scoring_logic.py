from models import Test


def calculate_points(guess: list, correct: list):
    """Базовая логика подсчета баллов. Сравнивает список ответов от пользователя со списком правильных ответов."""
    score = 0
    for i in range(len(guess)):
        if guess[i] == correct[i]:
            score += 1
    return score
