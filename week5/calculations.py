import json
from operator import *
from math import *


oper_dict = {'add': add, 'truediv': truediv, 'sub': sub,
             'mul': mul, 'pow': pow, 'floordiv': floordiv,
             'and': and_, 'xor': xor, 'or': or_,
             'is': is_, 'is_not': is_not, 'lshift': lshift,
             'mod': mod, 'rshift': rshift, 'lt': lt, 'le': le,
             'eq': eq, 'ne': ne, 'gt': gt, 'ge': ge, 'hypot': hypot,
             'atan2': atan2, 'ldexp': ldexp}
opers_list = list(oper_dict.keys())
opers = json.dumps(opers_list, indent=0)


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
