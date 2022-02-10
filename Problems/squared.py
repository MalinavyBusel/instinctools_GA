def problem(given):
    given = given.replace(' ', '')
    first = given.partition('x^2')
    a = int(first[0])
    if a == 0:
        return 'Ваше уравнение не квадратное, попробуйте снова'
    second = first[2].partition('x')
    b = int(second[0])
    c = int(second[2])
    D = b**2 - 4*a*c
    if D < 0:
        return 'No solutions'
    elif D == 0:
        res = -b/(2*a)
        return res
    else:
        x1 = (-b-D**0.5)/(2*a)
        x2 = (-b+D**0.5)/(2*a)
        return f'{x1}, {x2}'


print(problem('5x^2 - 4x + 2'))
print(problem('0x^2 - 7x + 2'))
