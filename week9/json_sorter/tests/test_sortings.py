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


def test_insertion_1():
    assert insertion_sort(unsorted_1) == sorted_1


def test_insertion_2():
    assert insertion_sort(unsorted_2) == sorted_2


def test_insertion_3():
    assert insertion_sort(unsorted_3) == sorted_3


def test_merge_1():
    assert merge_sort(unsorted_1) == sorted_1


def test_merge_2():
    assert merge_sort(unsorted_2) == sorted_2


def test_merge_3():
    assert merge_sort(unsorted_3) == sorted_3


def test_quick_sort_1():
    assert quick_sort(unsorted_1) == sorted_1


def test_quick_sort_2():
    assert quick_sort(unsorted_2) == sorted_2


def test_quick_sort_3():
    assert quick_sort(unsorted_3) == sorted_3


def test_shaking_1():
    assert shaking_sort(unsorted_1) == sorted_1


def test_shaking_2():
    assert shaking_sort(unsorted_2) == sorted_2


def test_shaking_3():
    assert shaking_sort(unsorted_3) == sorted_3
