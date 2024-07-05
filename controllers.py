from repository.sql_repository import SqliteRepository
from scoring_logic import calculate_points
from models import Test

repo = SqliteRepository()


def adder_controller(item: Test):
    """Контроллер для добавления теста в базу."""
    repo.add_test(item)


def username_validation(username):
    """Проверяет наличие введенного пользователем юзернейма в базе зарегистрированных пользователей.
    Пока нереализовано."""
    return True


def admin_validation():
    """Проверяет, имеет ли пользователь права администратора. Требует для работы базу пользователей,
     поэтому пока тоже нереализовано"""
    return True


def show_controller(test_id):
    """Контроллер-связка, достающий запрошенный тест из репозитория и отдающий его дальше.
     Все еще требует технические айдишники тестов, возможно придется переделывать."""
    item = repo.pull(test_id)
    return item


def show_all_controller():
    tests = repo.get_tests()
    return tests


def score_controller(test_id, guess: list, correct: list, username):
    """Контроллер, отвечающий за подсчет и занесение результатов пройденного теста.
     Пока не поддерживает создание новых пользователей."""
    score = calculate_points(guess, correct)
    user = repo.get_user(username)
    repo.add_result(score, user.userid, test_id)
    return score
