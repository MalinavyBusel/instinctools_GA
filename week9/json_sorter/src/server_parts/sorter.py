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


def pool_sorter(selected_sort: str, sequence: list, write_to_db: tuple=None):
    sorting_function = sorting_funcs[selected_sort]
    sorting_process = sorting_pool.submit(time_measurer, sorting_function, sequence)

    if write_to_db:
        def insert_data():
            hashed = write_to_db[0]
            database = write_to_db[1]
            db_data = dict()
            db_data['hashed_sequence'] = hashed
            db_data['sorted_sequence'] = sorting_process.result()['sorted_sequence']
            database.insert_one{db_data}
        sorting_process.add_done_callback(insert_data)

    return sorting_process.result()

