from operator import *


oper_dict = {'sum': add, 'div': truediv, 'diff': sub,
             'mult': mul, 'expon': pow, 'floordiv': floordiv,
             'and': and_, 'xor': xor, 'or': or_,
             'is': is_, 'is_not': is_not, 'lshift': lshift,
             'mod': mod, 'rshift': rshift, 'lt': lt, 'le': le,
             'eq': eq, 'ne': ne, 'gt': gt, 'ge': ge}


def calculate(expression: str):
    try:
        oper, val1, val2 = expression.strip().split(' ')
        res = oper_dict[oper](float(val1), float(val2))
        return str(res) + ':::'
    except ZeroDivisionError:
        return ':::You are trying to divide by zero.'
    except KeyError:
        return ':::There is no such operation.'
    except ValueError:
        return ':::Invalid arguments or their types.'