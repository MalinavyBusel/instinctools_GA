from collections import Counter, namedtuple


def parse_molecule(formula):
    # Первое значение - был ли последний символ цифрой, 2-е - буквой
    Last = namedtuple('Last', 'digit char')
    last = Last(False, False)

    # Делим формулу на симоволы для последующей обработки:
    formlist = list(formula)

    for i in range(len(formlist)):
        if formlist[i].isdigit():
            # Если последний символ не был цифрой - ставит перед ним знак умножения
            if not last[0]:
                formlist[i] = f'*{formlist[i]}'
            last = (True, False)

        elif formlist[i].isalpha():
            # Если символ это заглавная(всегда начало нового элемента), а перед ним буква или цифра
            # - ставит перед этим символом плюс
            if (last[1] or last[0]) and formlist[i].isupper():
                formlist[i] = f'+":{formlist[i]}"'

            # Если буква маленькая - то это продолжение другого элемента
            elif formlist[i].islower():
                formlist[i] = f'"{formlist[i]}"'

            # Если перед буквой скобка - ставим разделитель
            else:
                formlist[i] = f'":{formlist[i]}"'
            last = (False, True)

        else:
            # Если символ это открывающая скобка:
            if formlist[i] in '{[(':
                # Если скобка соседняя с цифрой или буквой, то нужен плюс для правильности счёта
                if last[1] or last[0]:
                    formlist[i] = f'+('

                # Иначе - просто меняем скобку на универсальную
                else:
                    formlist[i] = f'('

            # Если скобка завершающая - меняем её на универсальную
            else:
                formlist[i] = f')'
            last = (False, False)

    form = ''.join(formlist)  # - Собираем всё в выражение

    # Пока не знаю, как переделать. В принципе, после eval получаю строку, поэтому это не так опасно,
    # но если нужно, то постараюсь придумать, как убрать эту конструкцию
    made_of = eval(form)[1::].split(':')  # -убираем лишний разделитель в начале и вычисляем итоговую строку
    return dict(Counter(made_of))  # - Считаем результаты


if __name__ == '__main__':
    print(parse_molecule('(H2O(H2O)2(Si)3)4'))
    print(parse_molecule('(H2O)'))
    print(parse_molecule('Mg(OH)2'))
    print(parse_molecule('K4[ON(SO3)2]2'))
    print(parse_molecule('C2H5OH'))
    print(parse_molecule('((OH)2)2'))
