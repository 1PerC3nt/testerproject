def pull(file, num):
    """Достает тест из файла. Все тесты хранятся в одном файле, разделяются строкой 'Splitter\n'.
    На вход получает путь к файлу и номер теста в базе"""
    result = []
    with open(file, 'r', encoding='utf-8') as f:
        for i in f.readlines():
            if i == 'Splitter\n':
                num -= 1
                continue
            if num == 1:
                result.append(i.strip())
        return result


temp = pull('storage.txt', 2)
print(temp)