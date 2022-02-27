def queue_time(people: list, number_of_registers: int):
    # reversing the list to make the deletions faster
    people.reverse()
    cash_registers = []

    # the first clients for every register
    for i in range(number_of_registers):
        cash_registers.append(people.pop())

    # simulating the real queue
    while people:
        minimal = min(cash_registers)  # minimal time taken(in other words, first empty cash register)
        min_index = cash_registers.index(minimal)
        cash_registers[min_index] = cash_registers[min_index] + people.pop()
    return max(cash_registers)


if __name__ == '__main__':
    assert queue_time([7, 5, 2, 3, 3, 1, 2, 6, 6, 8, 4, 3], 3) == 17
    assert queue_time([5, 3, 4], 1) == 12
    assert queue_time([10, 2, 3, 3], 2) == 10
    assert queue_time([2, 3, 10], 2) == 12
