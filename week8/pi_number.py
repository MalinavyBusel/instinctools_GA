import multiprocessing as mp

from random import random


def count_pi(shared_val, total):
    in_circle = 0
    for i in range(total):
        pair = (random(), random())
        squared_sum = pair[0]**2 + pair[1]**2
        if squared_sum < 1:
            in_circle += 1
    with shared_val.get_lock():
        shared_val.value += in_circle


def get_pi(total=20000):
    in_circle_total = mp.Value('i', 0)
    processes = []
    cores = mp.cpu_count()
    one_process_range = int(total/cores)
    for proc in range(cores):
        p = mp.Process(target=count_pi, args=(in_circle_total, one_process_range))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()
    return in_circle_total.value/total*4


if __name__ == '__main__':
    print(get_pi())
