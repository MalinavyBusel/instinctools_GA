import concurrent.futures as cf

from typing import Callable

from sortings.merge_sort import merge_sort
from sortings.quick_sort import quick_sort
from sortings.shaking import shaking_sort
from sortings.insertions import insertion_sort

from server_parts.context_timer import Timer


sorting_pool = cf.ProcessPoolExecutor()
sorting_funcs = {"merge_sort": merge_sort,
                 "quick_sort": quick_sort,
                 "shaking_sort": shaking_sort,
                 "insertion_sort": insertion_sort}


def time_measurer(func: Callable, sequence: list):
    sort_timer = Timer()
    with sort_timer:
        sorted_sequence = func(sequence)
    result = {'time_taken': sort_timer.total_time,
              'sorted_sequence': sorted_sequence}
    return result


def pool_sorter(selected_sort: str, sequence: list):
    sorting_function = sorting_funcs[selected_sort]
    sorting_process = sorting_pool.submit(time_measurer, sorting_function, sequence)
    return sorting_process.result()

