from repository import sql_repository


repo = sql_repository.SqliteRepository()

data = repo.pull(1)
user = repo.get_user('Amogus')
print(user)



