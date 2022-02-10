lst = [(0, 'h'), (4, 'o'), (2, 'l'), (1, 'e'), (3, 'l')]


def checker(given_list):
    starts = True
    for elem in given_list:
        lst1 = [type(elem) != "<class 'tuple'>", not elem[0].isdigit(), type(elem[1]) != "<class 'str'>"]
        if any(lst1):
            starts = False
    if starts:
        return repair(given_list)
    else:
        return 'Wrong input. Please, try again.'


def repair(given_list):
    my_dict = dict(given_list)
    my_str = ''
    for i in range(len(given_list)):
        my_str += my_dict[i]
    return my_str


