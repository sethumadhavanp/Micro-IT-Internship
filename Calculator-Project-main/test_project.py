from project import find_operation, add, multiply

def test_add():
    assert add(5,2) == 7

def test_find_operation():
    operation = "-"
    assert find_operation(operation) == (True, "-")

def test_multiply():
    assert multiply (5,6) == 30

