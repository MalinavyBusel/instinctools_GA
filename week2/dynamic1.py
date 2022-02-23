from collections import defaultdict


def cash_variants(total_sum: int, cents: list):
    '''Returns a set of different variants how to get necessary sum in format
    "n{number1}:total_times n{number2}:total_times ... n{numberN}:total_times"'''

    variants_set = set()
    num_count = defaultdict(int)
    variant_counter(total_sum, num_count, cents, variants_set)
    return variants_set


def variant_counter(num: int, num_count: defaultdict, cents: list, variants_set: set):
    for cent in cents:
        num1 = num
        num_count1 = num_count.copy()
        num1 -= cent
        num_count1[cent] += 1

        # if n == 0 then write variant to a set
        if num1 == 0:
            variant = ''
            for cent in cents:
                variant += 'n' + str(cent) + ':' + str(num_count1[cent])+' '
            variants_set.add(variant[:-1])

        # else if n > 0 then we need to subtract more nums
        elif num1 > 0:
            variant_counter(num1, num_count1.copy(), cents, variants_set)

        # else if n < 0 func is stopped


if __name__ == '__main__':
    print(cash_variants(10, [1, 2, 5]))
