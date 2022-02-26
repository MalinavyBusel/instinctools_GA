from typing import Callable


class NotValidArguments(Exception):
    pass


def func_validator(args: list,  hints: list,  final_func: Callable, *params: list,):
    assert len(args) == len(hints)

    wrong_args = ''

    for i in range(len(args)):
        if type(args[i]) != hints[i]:
            param = f'"{params[i]}" ' if params else f'{i}th '
            inform_str = f'----- The argument of the {final_func} parameter {param}' \
                         f'is of a wrong type:\n' \
                         f'          needed {hints[i]}, get {type(args[i])}\n'
            wrong_args += inform_str

    if wrong_args:
        wrong_args = '\n' + wrong_args
        raise NotValidArguments(wrong_args)

    # if everything is correct, the validated function starts
    final_func(*args)


func_validator(['10'], [list], print)

