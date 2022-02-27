from random import randint
from time import time
from insertions import insertion_sort
from quick_sort import quick_sort
from shaking import shaking_sort
from merge_sort import merge_sort


def sort_timer(n: int):
    '''Show actually useful results with n starting from 1000-2000'''
    lst = [randint(-500, 1000) for i in range(n)]
    start = time()
    insertion_sort(lst)
    step1 = time()
    quick_sort(lst)
    step2 = time()
    shaking_sort(lst)
    step3 = time()
    merge_sort(lst)
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
    print(sort_timer(3000))
