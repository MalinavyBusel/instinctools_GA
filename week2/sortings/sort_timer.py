from random import randint
from time import time
from insertions import insertion_sort
from quick_sort import quick_sort
from shaking import shaking_sort
from merge_sort import merge_sort

lst = [randint(-500, 1000) for i in range(3000)]


def sort_timer(sorted_list: list):
    start = time()
    insertion_sort(sorted_list)
    step1 = time()
    quick_sort(sorted_list)
    step2 = time()
    shaking_sort(sorted_list)
    step3 = time()
    merge_sort(sorted_list)
    step4 = time()
    insertions = step1 - start
    quick = step2 - step1
    shake = step3 - step2
    merge = step4 - step3
    return (f'''insertion_sort: {insertions},
quick_sort: {quick},
shaking_sort: {shake},
merge_sort: {merge}''')


if __name__ == '__main__':
    print(sort_timer(lst))
