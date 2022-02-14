from enum import Enum

my_days = {'понедельник': 5,
           'пн': 5,
           'monday': 5,
           'вторник': 4,
           'вт': 4,
           'tuesday': 4,
           'среда': 3,
           'ср': 3,
           'wednesday': 3,
           'четверг': 2,
           'чт': 2,
           'thursday': 2,
           'пятница': 1,
           'пт': 1,
           'friday': 1,
           'суббота': 1,
           'сб': 1,
           'saturday': 1,
           'воскресенье': 6,
           'вс': 6,
           'sunday': 6}


def days(my_days: dict):
    day = input('Введите день недели: ').lower()

    to_wait = my_days.setdefault(day, 'smth')
    if to_wait == 1:
        return 'You have to wait q day.'
    elif to_wait in [2, 3, 4, 5, 6]:
        return f'You have to wait {to_wait} days.'
    else:
        return 'No such day'


if __name__ == '__main__':
    print(days(my_days))
