# assert test [, msg]
def write_data(file, data):
    assert file, "write_data: файл не определен!"
    # ...


def assert_equal(x, y):
    assert x == y, "{} != {}".format(x, y)