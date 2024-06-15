from repository import sql_repository


repo = sql_repository.SqliteRepository()

data = repo.pull(1)

print(data)


