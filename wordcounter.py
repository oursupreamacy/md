m = input("Введите имя файла: ")

with open(m, 'r', encoding='utf-8') as f:
    d = {}
    s = f.read()
    s = s.lower()
    s = s.split()
    for x in s:
        if x not in d:
            d[x] = 1
        else:
            d[x] += 1
    l = lambda z: z[1]
    print(sorted(d.items(), key=l, reverse=True))
