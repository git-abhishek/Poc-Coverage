from arithmetic.operations import add, sub


def test_add():
    assert add(5, 6) == 11


def test_sub():
    assert sub(5, 2) == 3