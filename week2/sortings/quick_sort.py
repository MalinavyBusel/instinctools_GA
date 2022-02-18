def quick_sort(iterable):
    if len(iterable) < 2:
        return iterable
    else:
        elem_to_compare = iterable[0]
        iterable1 = [i for i in iterable[1:] if i < elem_to_compare]
        iterable2 = [i for i in iterable[1:] if i >= elem_to_compare]
        return quick_sort(iterable1) + [elem_to_compare] + quick_sort(iterable2)


if __name__ == '__main__':
    print(quick_sort([3, 73, 1, 8, 4, 8, 3, 34, 87, 3, 11, 6, 1, 7, 4, 6, 2, 464, 9]))
    print(quick_sort([3, 73, 1, 8, 4, 8, 6, -1, 3, 3, 34, 87, 3, 0, 51, -10, 5, 11, 6, 1, 7, 4, 6, 2, 464, 9]))
