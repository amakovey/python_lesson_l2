from contextlib import contextmanager


@contextmanager
def ListTransaction(thelist):
    workingcopy = list(thelist)
    yield workingcopy
    # Изменить оригинальный список, только если не возникло ошибок
    thelist[:] = workingcopy

items = [1,2,3]
with ListTransaction(items) as working:
    working.append(4)
    working.append(5)
    print(items) # Выведет [1,2,3,4,5]

try:
    with ListTransaction(items) as working:
        working.append(6)
        working.append(7)
        raise RuntimeError("Немного смошенничаем!")
except RuntimeError:
    pass #Никогда так не делай! :)

print(items) # Выведет [1,2,3]