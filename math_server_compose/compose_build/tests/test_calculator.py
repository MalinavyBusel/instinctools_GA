from calc_processing.calculations import calculate


def test_operation_1():
    res, error = calculate('add 3 3').split(':::')
    assert res == '6'


def test_operation_2():
    res, error = calculate('mod 10 6').split(':::')
    assert res == '4'


def test_operation_3():
    res, error = calculate('pow 5 7').split(':::')
    assert res == '78125.0'


def test_operation_4():
    res, error = calculate('and 5 7').split(':::')
    assert res == '5'


def test_operation_5():
    res, error = calculate('add 3 3').split(':::')
    assert res == '6'


def test_operation_6():
    res, error = calculate('is_not 1 1.0').split(':::')
    assert res == 'True'


def test_operation_7():
    res, error = calculate('lt 1 3').split(':::')
    assert res == 'True'


def test_zero_division():
    res, error = calculate('truediv 3 0').split(':::')
    assert error == 'You are trying to divide by zero.'


def test_invalid_operator():
    res, error = calculate('multiply 3 3').split(':::')
    assert error == 'There is no such operation.'


def test_invalid_value():
    res, error = calculate('add a b').split(':::')
    assert error == 'Invalid arguments or their types.'
