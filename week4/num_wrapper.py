from operator import *


too_big_index = IndexError()


class NumWrapper:
    def __init__(self, *nums: int):
        self.nums = list(nums)

    def __getitem__(self, index_: int):
        if not index_ < len(self.nums):
            raise too_big_index
        return self.nums[index_]

    def __setitem__(self, index_: int, num: int):
        if not index_ < len(self.nums):
            raise too_big_index
        self.nums[index_] = num
        return None

    def append(self, num: int):
        self.nums.append(num)
        return None

    def remove(self, num: int):
        self.nums.remove(num)
        return None

    def pop(self, index_: int = -1):
        if not index_ < len(self.nums):
            raise too_big_index
        return self.nums.pop(-1)

    def __len__(self):
        return len(self.nums)

    def min_iter(self, other: 'NumWrapper'):
        minlen = min(len(self), len(other))
        return minlen

# All comparison methods are implemented without comparing the length
# of wrappers. Comparing with the length of wrappers in all 6
# methods below could be easily done with:
# "return self.nums <=\>=\... other.nums"
    def __gt__(self, other: 'NumWrapper'):
        minlen = self.min_iter(other)
        for ind in range(minlen):
            if self[ind] <= other[ind]:
                return False
        return True

    def __le__(self, other: 'NumWrapper'):
        return not self.__gt__(other)

    def __lt__(self, other: 'NumWrapper'):
        minlen = self.min_iter(other)
        for ind in range(minlen):
            if self[ind] >= other[ind]:
                return False
        return True

    def __ge__(self, other: 'NumWrapper'):
        return not self.__lt__(other)

    def __eq__(self, other: 'NumWrapper'):
        minlen = self.min_iter(other)
        for ind in range(minlen):
            if self[ind] != other[ind]:
                return False
        return True

    def __ne__(self, other: 'NumWrapper'):
        return not self.__eq__(other)

# Magic methods for division
    def zipper(self, other: 'NumWrapper'):
        return list(zip(self.nums, other.nums))

    def __truediv__(self, other: 'NumWrapper'):
        def division(pair: list):
            a = pair[0]
            b = pair[1]
            return float('nan') if not pair[1] else truediv(a, b)
        res = list(map(division, self.zipper(other)))
        return NumWrapper(*res)

    def __floordiv__(self, other: 'NumWrapper'):
        def division(pair: list):
            a = pair[0]
            b = pair[1]
            return float('nan') if not pair[1] else floordiv(a, b)
        res = list(map(division, self.zipper(other)))
        return NumWrapper(*res)

    def __mod__(self, other: 'NumWrapper'):
        def division(pair: list):
            a = pair[0]
            b = pair[1]
            return float('nan') if not pair[1] else mod(a, b)
        res = list(map(division, self.zipper(other)))
        return NumWrapper(*res)

# Addition, subtraction, multiplication
    def __add__(self, other: 'NumWrapper'):
        def addition(pair: list):
            a = pair[0]
            b = pair[1]
            return add(a, b)
        res = list(map(addition, self.zipper(other)))
        return NumWrapper(*res)

    def __mul__(self, other: 'NumWrapper'):
        def mult(pair: list):
            a = pair[0]
            b = pair[1]
            return mul(a, b)
        res = list(map(mult, self.zipper(other)))
        return NumWrapper(*res)

    def __sub__(self, other: 'NumWrapper'):
        def subtr(pair: list):
            a = pair[0]
            b = pair[1]
            return sub(a, b)
        res = list(map(subtr, self.zipper(other)))
        return NumWrapper(*res)


if __name__ == '__main__':
    wr1 = NumWrapper(1, 2, 3)
    wr2 = NumWrapper(1, 2, 3)
    wr3 = wr1/wr2
    print(wr3.nums)
    wr4 = wr1+wr2
    print(wr4.nums)
