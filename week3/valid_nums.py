from operator import *


input_dict = {'sum': {'min': 5, 'max': 50},
              'div': {'min': 2, 'max': 10},
              'diff': {'min': 5, 'max': 20}}


class NotValidInputNumbers(Exception):
    pass


def nums_validator(num1: int, num2: int, input_dict: dict):
    res_dict = {'sum': add,
                'div': truediv,
                'diff': sub,
                'mult': mul,
                'expon': pow}
    rangeouts = ''
    for key in input_dict.keys():
        res = res_dict[key](num1, num2)
        r_min = input_dict[key]['min']
        r_max = input_dict[key]['max']
        if out_of_range(res, r_min, r_max):
            inform_str = f'----- The result of {key} of num1 and num2 ' \
                         f'({res}) is out of range[{r_min}; {r_max}]\n'
            rangeouts += inform_str
    if rangeouts:
        rangeouts = '\n'+rangeouts
        raise NotValidInputNumbers(rangeouts)


def out_of_range(num, minimal, maximum, soft=True):
    if soft:
        return any([num <= minimal, num >= maximum])
    else:
        return any([num < minimal, num > maximum])


nums_validator(500, 100, input_dict)
