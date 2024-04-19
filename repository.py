def pull(file, num):
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