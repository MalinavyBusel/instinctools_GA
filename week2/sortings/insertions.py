def insertion_sort(iterable):
    iter_output = []
    iter_output.append(iterable.pop())  # taking element from the end in order not to move other elements to the start
    # Going through the list and sorting it
    for elem in iterable:
        start = 0
        stop = len(iter_output)
        binary(elem, start, stop, iter_output)
    return iter_output


# Using binary search, define the place to insert the num
def binary(num, start, stop, iterable_to_out):
    # Base case
    if stop - start == 1:
        if num >= iterable_to_out[start]:
            iterable_to_out.insert(start + 1, num)
        else:
            iterable_to_out.insert(start, num)

    # Recursive case
    else:
        index_to_compare = int((start + stop) / 2)
        if iterable_to_out[index_to_compare] <= num:
            binary(num, index_to_compare, stop, iterable_to_out)
        else:
            binary(num, start, index_to_compare, iterable_to_out)


if __name__ == '__main__':
    print(insertion_sort([3, 73, 1, 8, 4, 8, 3, 34, 87, 3, 11, 6, 1, 7, 4, 6, 2, 464, 9]))
    print(insertion_sort([3, 73, 1, 8, 4, 8, 6, -1, 3, 3, 34, 87, 3, 0, 51, -10, 5, 11, 6, 1, 7, 4, 6, 2, 464, 9]))
