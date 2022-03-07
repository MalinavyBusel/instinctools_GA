class NumWrapper:
    def __init__(self, *nums: int):
        self.nums = [*nums]

    def __getitem__(self, index: int):
        if not index < len(self.nums):
            raise IndexError
        return self.nums[index]

    def __setitem__(self, index: int, num: int):
        if not index < len(self.nums):
            raise IndexError
        self.nums[index] = num

    def append(self, num: int):
        self.nums.append(num)

    def remove(self, num: int):
        self.nums.remove(num)

    def pop(self, index: int = -1):
        if not index < len(self.nums):
            raise IndexError
        return self.nums.pop(-1)

    def __len__(self):
        return len(self.nums)

    def min_iter(self, other):
        minlen = min(len(self), len(other))
        return minlen

# All comparison methods are implemented without comparing the length
# of wrappers. Comparing with the length of wrappers in all 6
# methods below could be easily done with:
# "return self.nums <=\>=\... other.nums"
    def __gt__(self, other):
        minlen = self.min_iter(other)
        for ind in range(minlen):
            if self[ind] <= other[ind]:
                return False
        return True

    def __le__(self, other):
        return not self.__gt__(other)

    def __lt__(self, other):
        minlen = self.min_iter(other)
        for ind in range(minlen):
            if self[ind] >= other[ind]:
                return False
        return True

    def __ge__(self, other):
        return not self.__lt__(other)

    def __eq__(self, other):
        minlen = self.min_iter(other)
        for ind in range(minlen):
            if self[ind] != other[ind]:
                return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

# Magic methods for division
    def zipper(self, other):
        return list(zip(self.nums, other.nums))

    def __truediv__(self, other):
        def division(pair: list):
            a = pair[0]
            b = pair[1]
            return float('nan') if not pair[1] else a.__truediv__(b)
        res = list(map(division, self.zipper(other)))
        return NumWrapper(*res)

    def __floordiv__(self, other):
        def division(pair: list):
            a = pair[0]
            b = pair[1]
            return float('nan') if not pair[1] else a.__floordiv__(b)
        res = list(map(division, self.zipper(other)))
        return NumWrapper(*res)

    def __mod__(self, other):
        def division(pair: list):
            a = pair[0]
            b = pair[1]
            return float('nan') if not pair[1] else a.__mod__(b)
        res = list(map(division, self.zipper(other)))
        return NumWrapper(*res)

# Addition, subtraction, multiplication
    def __add__(self, other):
        def addition(pair: list):
            a = pair[0]
            b = pair[1]
            return a.__add__(b)
        res = list(map(addition, self.zipper(other)))
        return NumWrapper(*res)

    def __mul__(self, other):
        def mult(pair: list):
            a = pair[0]
            b = pair[1]
            return a.__mul__(b)
        res = list(map(mult, self.zipper(other)))
        return NumWrapper(*res)

    def __sub__(self, other):
        def sub(pair: list):
            a = pair[0]
            b = pair[1]
            return a.__sub__(b)
        res = list(map(sub, self.zipper(other)))
        return NumWrapper(*res)


if __name__ == '__main__':
    wr1 = NumWrapper(1, 2, 3)
    wr2 = NumWrapper(1, 2, 3)
    wr3 = wr1/wr2
    print(wr3.nums)
    wr4 = wr1+wr2
    print(wr4.nums)
