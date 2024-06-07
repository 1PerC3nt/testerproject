from repository.json_repository import adder_json, integrity_check, pull
from models import Test


def adder_controller(item: Test):
    """Контроллер для добавления теста в базу.
     Проверяет целостность собранного объекта и вызывает функцию из репозитория."""
    if integrity_check(item):
        adder_json(item)
    else:
        raise ValueError


def username_validation(username):
    """Проверяет наличие введенного пользователем юзернейма в базе зарегистрированных пользователей.
    Пока нереализовано."""
    return True


def admin_validation():
    """Проверяет, имеет ли пользователь права администратора. Требует для работы базу пользователей,
     поэтому пока тоже нереализовано"""
    return True


def show_controller(testid: str):
    """Контроллер-связка, достающий запрошенный тест из репозитория и отдающий его дальше.
     Все еще требует технические айдишники тестов, возможно придется переделывать."""
    item = pull(testid)
    return item

