import foo
def bar():
    x = 13
    def helloworld():
        return "Привет, Мир! x = %d" % x

    print(helloworld.__closure__[0].cell_contents)
    return foo.callf(helloworld)

print(bar()) #Привет, Мир! x = 13



