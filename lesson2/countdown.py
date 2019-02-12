def countdown(n):
    e = 0
    def next():
        nonlocal n, e
        e += 1
        r = n
        n -= 1
        return r
    return next

# Пример использования
next = countdown(10)
print(next.__closure__[0].cell_contents)
print(next.__closure__[1].cell_contents)
print("\n")
while True:
    v = next() # Получить следующее значение
    print(v)
    if not v: break
    