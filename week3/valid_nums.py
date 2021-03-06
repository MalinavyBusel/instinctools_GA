import pathlib
import yaml

from operator import *


class NotValidInputNumbers(Exception):
    pass


def nums_validator(num1: int, num2: int, file_name: str):

    file_path = pathlib.Path(file_name)
    with file_path.open("r") as f:
        input_dict = yaml.safe_load(f)

    rangeouts = ''
    res_dict = {'sum': add, 'div': truediv, 'diff': sub,
                'mult': mul, 'expon': pow, 'floordiv': floordiv,
                'and': and_, 'xor': xor, 'or': or_,
                'is': is_, 'is_not': is_not, 'lshift': lshift,
                'mod': mod, 'rshift': rshift, 'lt': lt, 'le': le,
                'eq': eq, 'ne': ne, 'gt': gt, 'ge': ge}

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


def out_of_range(num: int, minimal: int, maximum: int, soft: bool=True):
    if soft:
        return any([num <= minimal, num >= maximum])
    else:
        return any([num < minimal, num > maximum])


if __name__ == '__main__':
    nums_validator(500, 100, 'my_yaml.yaml')
