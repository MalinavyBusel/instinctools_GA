from enum import Enum


class Days(Enum):
    понедельник = 5
    пн = 5
    monday = 5
    вторник = 4
    вт = 4
    tuesday = 4
    среда = 3
    ср = 3
    wednesday = 3
    четверг = 2
    чт = 2
    thursday = 2
    пятница = 1
    пт = 1
    friday = 1
    суббота = 1
    сб = 1
    saturday = 1
    воскресенье = 6
    вс = 6
    sunday = 6


def days():
    accepted = {'sunday', 'вс', 'воскресенье', 'saturday', 'сб', 'суббота', 'friday', 'пт', 'пятница', 'чт',
                'четверг', 'ср', 'среда', 'вт', 'вторник', 'пн',
                'понедельник', 'monday', 'tuesday', 'wednesday', 'thursday'}
    day = input('Введите день недели: ').lower()

    # При надобности могу сделать без eval, но тогда, наверное, придется убрать Enum
    if day in accepted:
        to_wait = eval(f'Days.{day}.value')
    else:
        print('Введите день корректно!')
        return days()
    if to_wait == 1:
        return 'Вам осталось ждать 1 день.'
    elif to_wait in [2, 3, 4, ]:
        return f'Вам осталось ждать {to_wait} дня.'
    elif to_wait in [5, 6, ]:
        return f'Вам осталось ждать {to_wait} дней.'


if __name__ == '__main__':
    print(days())
