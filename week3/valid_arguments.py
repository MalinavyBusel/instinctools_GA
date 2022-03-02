from typing import Callable


class NotValidArguments(Exception):
    pass


def validator(func: Callable):
    import inspect

    def wrapper(*args):
        func_params = inspect.getfullargspec(func).annotations
        wrong_args = ''

        for i, key in enumerate(func_params.keys()):
            value = func_params[key]
            if not isinstance(args[i], value):
                param = f'"{key}" '
                inform_str = f'----- The argument of the {func} parameter {param}' \
                             f'is of a wrong type:\n' \
                             f'          needed {value}, got {type(args[i])}\n'
                wrong_args += inform_str

        if wrong_args:
            wrong_args = '\n' + wrong_args
            raise NotValidArguments(wrong_args)
        else:
            return func(*args)

    return wrapper


@validator
def smthng(val1: int, val2: str):
    print(val1*val2)


smthng(5, 3)
