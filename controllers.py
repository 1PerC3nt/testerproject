from repository.sql_repository import SqliteRepository
from models import Test

repo = SqliteRepository()


def adder_controller(item: Test):
    """Контроллер для добавления теста в базу."""
    repo.adder_sql(item)


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
    item = repo.pull(testid)
    return item
