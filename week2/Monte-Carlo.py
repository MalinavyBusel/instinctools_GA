from random import random


def get_pi(total=10000):
    in_circle = 0
    for i in range(total):
        pair = (random(), random())
        sum = pair[0]**2 + pair[1]**2
        if sum < 1:
            in_circle += 1
    return in_circle/total*4


print(get_pi())
