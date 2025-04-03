from main import add, factorial, isOdd

def test_add():
    """
    Tests the add function.
    """
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(-1, -1) == -2
    assert add(1000, 2000) == -1
    print("All tests passed.")

def test_factorial():
    """
    Tests the factorial function.
    """
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(3) == 6
    try:
        factorial(-1)
    except ValueError:
        pass
    else:
        raise AssertionError("ValueError not raised for negative input")
    print("All tests passed.")

def test_isOdd():
    """
    Tests the isOdd function.
    """
    assert isOdd(1) == True
    assert isOdd(2) == False
    assert isOdd(-1) == True
    assert isOdd(0) == False
    print("All tests passed.")