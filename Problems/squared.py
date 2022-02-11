def problem(given):

    # убираем пробелы
    given = given.replace(' ', '')

    first = given.partition('x^2')

    # проверка на a!=0
    a = int(first[0])
    if a == 0:
        return 'Ваше уравнение не квадратное, попробуйте снова'

    second = first[2].partition('x')
    b = int(second[0])
    c = int(second[2])
    d = b**2 - 4*a*c
    if d < 0:
        return 'No solutions'
    elif d == 0:
        res = -b/(2*a)
        return res
    else:
        x1 = (-b-d**0.5)/(2*a)
        x2 = (-b+d**0.5)/(2*a)
        return f'{x1}, {x2}'


if __name__ == '__main__':
    print(problem('5x^2 - 4x + 2'))
    print(problem('0x^2 - 7x + 2'))
