from bank import value



def test_hello_value():
    assert value("hello") == 0
    assert value("Hello") == 0


def test_hi_value():
    assert value("h") == 20
    assert value("Hey") == 20


def test_random_value():
    assert value("yo") == 100


