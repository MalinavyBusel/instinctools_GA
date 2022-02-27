from random import random


def get_pi(total=10000):
    in_circle = 0
    for i in range(total):
        pair = (random(), random())
        squared_sum = pair[0]**2 + pair[1]**2
        if squared_sum < 1:
            in_circle += 1
        # in_circle += 1 if (random()**2+random()**2)<1 else in_circle
    return in_circle/total*4


if __name__ == '__main__':
    print(get_pi())
