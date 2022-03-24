import json

from .config import settings

oper_dict = settings.oper_dict
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
