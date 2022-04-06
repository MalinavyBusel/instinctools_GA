import multiprocessing as mp
import concurrent.futures as cf

from random import random


def count_pi(total: int):
    in_circle = 0
    for i in range(total):
        pair = (random(), random())
        squared_sum = pair[0]**2 + pair[1]**2
        if squared_sum < 1:
            in_circle += 1
    return in_circle


def get_pi(total=20000):
    in_circle_total = 0
    cores = mp.cpu_count()
    one_process_range = int(total/cores)

    executor = cf.ProcessPoolExecutor()

    shared_val_list = [in_circle_total for i in range(cores)]
    one_proc_range_list = [one_process_range for i in range(cores)]
    futures = executor.map(count_pi, shared_val_list, one_proc_range_list)

    for result in futures:
        in_circle_total += result
    return in_circle_total/total*4


if __name__ == '__main__':
    print(get_pi())
