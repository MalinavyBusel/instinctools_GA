def shaking_sort(iterable: list):
    i, j = 0, len(iterable)
    while i < j:
        for k in range(i, j - 1):
            if iterable[k] >= iterable[k + 1]:
                iterable[k], iterable[k + 1] = iterable[k + 1], iterable[k]
        j -= 1
        for m in range(j, i, -1):
            if iterable[m] <= iterable[m - 1]:
                iterable[m], iterable[m - 1] = iterable[m - 1], iterable[m]
        i += 1
    return iterable

if __name__ == '__main__':
    print(shaking_sort([3, 73, 1, 8, 4, 8, 3, 34, 87, 3, 11, 6, 1, 7, 4, 6, 2, 464, 9]))
    print(shaking_sort([3, 73, 1, 8, 4, 8, 6, -1, 3, 3, 34, 87, 3, 0, 51, -10, 5, 11, 6, 1, 7, 4, 6, 2, 464, 9]))
