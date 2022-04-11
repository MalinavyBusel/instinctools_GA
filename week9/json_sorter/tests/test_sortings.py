from sortings.insertions import insertion_sort
from sortings.merge_sort import merge_sort
from sortings.quick_sort import quick_sort
from sortings.shaking import shaking_sort

unsorted_1 = [3, 73, 1, 8, 4, 8, 34, 87, 11]
unsorted_2 = [-1, 34, 87, 3, 0, 51, -10, 5, 11, 6, 1, 7, 4]
unsorted_3 = [74, 19.001, -345, 0, 5823, 7.1, 8, 12.84, -23.56, 10, 893]
sorted_1 = [1, 3, 4, 8, 8, 11, 34, 73, 87]
sorted_2 = [-10, -1, 0, 1, 3, 4, 5, 6, 7, 11, 34, 51, 87]
sorted_3 = [-345, -23.56, 0, 7.1, 8, 10, 12.84, 19.001, 74, 893, 5823]


def test_1():
    assert insertion_sort(unsorted_1) == merge_sort(unsorted_1) \
           == quick_sort(unsorted_1) == shaking_sort(unsorted_1)


def test_2():
    assert insertion_sort(unsorted_2) == merge_sort(unsorted_2) \
           == quick_sort(unsorted_2) == shaking_sort(unsorted_2)


def test_3():
    assert insertion_sort(unsorted_3) == merge_sort(unsorted_3) \
           == quick_sort(unsorted_3) == shaking_sort(unsorted_3)
