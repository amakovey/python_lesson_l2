import pickle

obj = ['ops', 12, (1, 2), {'abc': 10}]


class Person:

    def __init__(self, name):
        self.name = name
        

print(obj)

p1 = Person('Иван')
p2 = Person('Леонид')

h = [obj, p1, p2]

with open('p.dat', 'wb') as f:
    pickle.dump(h, f)

with open('p.dat', 'rb') as f:
    result = pickle.load(f)
    print(result)
    print(result[1].name)