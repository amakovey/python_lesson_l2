enable_tracing = True
if enable_tracing:
    debug_log = open("debug.log", "w", encoding='utf-8')


def trace(func):
    if enable_tracing:
        def callf(*args, **kwargs):
            debug_log.write("Вызов %s: %s, %s\n" % (func.__name__, args, kwargs))
            r = func(*args, **kwargs)
            debug_log.write("%s вернула %s\n" % (func.__name__, r))
            return r

        return callf
    else:
        return func


def some_decorator(func):
    def dop_func():
        print("Do something before")
        func()
        print("Do something after")

    return dop_func


def some_decorator2(func):
    def dop_func(*args):
        print("Do something")
        return func(*args)

    return dop_func


@trace
def square(x):
    return x * x


@some_decorator
def show_some():
    print("Hello!")


@some_decorator2
def pow(x, val):
    return x ** val


square(3)
show_some()
print(pow(2, 4))

print(pow(3, 3))
