from collections import Counter
from enum import Enum


class Actions(Enum):
    deletion = 'd'
    insertion = 'i'
    transposition = 't'
    replacement = 'r'
    nothing_to_do = 'n'


def levenshtein(origin_string: str, compare_string: str, weights: list, logging: str = False):
    ''' weights:
            replace - weights[0]
            insert - weights[1]
            delete - weights[2]
            transpose - weights[3]
        logging:
            False - no logs
            "on" - returns (x, y) of table for letter in str1 and reuqired operation for this letter
            "count" - returns the total number of every operation needed(in Counter object)'''
    matrix = []
    for y in range(len(origin_string)):
        matrix.append(list())
        for x in range(len(compare_string)):
            matrix[y].append(distance(x, y, compare_string, origin_string, matrix, weights))
    res = matrix[-1][-1][0]
    if logging:
        return res, loggs(matrix, logging)
    return res


def loggs(matrix: list, logging: str):
    ''' Returns needed actions with origin_string to transform it into compare_string'''
    str1_logs = {}
    x = len(matrix[0])-1
    y = len(matrix) - 1
    while True:
        action = matrix[y][x][1]
        if action != Actions.nothing_to_do.value:
            str1_logs[(x, y)] = action
        if action == Actions.replacement.value or action == Actions.nothing_to_do.value:
            x -= 1
            y -= 1
        elif action == Actions.insertion.value:
            x -= 1
        elif action == Actions.deletion.value:
            y -= 1
        elif action == Actions.transposition.value:
            x -= 2
            y -= 2
        if x < 0 and y < 0:
            break
    if logging == 'count':
        return Counter(str1_logs.values())
    return str1_logs


def distance(x: int, y: int, str2, str1, matrix: list, weights: list):
    ''' A function to choose the most suitable operation in a definite situation '''
    to_compare = []

    # replacement
    if x >= 1 and y >= 1:
        # checks whether letters are equal or not
        replace_val = matrix[y-1][x-1][0]
        to_compare.append([replace_val if str1[y] == str2[x] else replace_val+weights[0],
                           'n' if str1[y] == str2[x] else 'r'])  # 'n' - nothing

    # insertion
    if x >= 1:
        insert_val = matrix[y][x-1][0]
        to_compare.append([insert_val+weights[1], 'i'])

    # deletion
    if y >= 1:
        del_val = matrix[y-1][x][0]
        to_compare.append([del_val+weights[2], 'd'])

    # transposition - changing the places of two neighbour letters
    if x-2 >= 0 and y-2 >= 0 and str1[y] == str2[x-1] and str1[y-1] == str2[x]:
        transpose_val = matrix[y - 2][x - 2][0]
        to_compare.append([transpose_val+weights[3], 't'])

    # first using of the function
    if x == 0 and y == 0:
        to_compare.append([0 if str1[y] == str2[x] else weights[0], 'n' if str1[y] == str2[x] else 'r'])
    return min(to_compare)


if __name__ == '__main__':
    assert levenshtein('кинотеатр', 'машина', [1, 1, 1, 1]) == 8
    assert levenshtein('маргарита', 'матрица', [1, 1, 1, 1]) == 4
