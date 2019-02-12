from urllib.request import urlopen
def page(url):
    def get():
        return urlopen(url).read()
    return get

python = page("http://www.python.org")
jython = page("http://www.jython.org")
# Какой-то другой код
# ...
# В нужном месте вызываем
pydata = python()
jydata = jython()
print(python.__closure__)
print(python.__closure__[0].cell_contents)