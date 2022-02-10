from collections import Counter, namedtuple


def parse_molecule(formula):
    Last = namedtuple('Last', 'digit char')
    last = Last(False, False)
    formlist = list(formula)
    for i in range(len(formlist)):
        if formlist[i].isdigit():

            if not last[0]:
                formlist[i] = f'*{formlist[i]}'

            last = (True, False)
        elif formlist[i].isalpha():

            if (last[1] or last[0]) and formlist[i].isupper():
                formlist[i] = f'+":{formlist[i]}"'
            elif formlist[i].islower():
                formlist[i] = f'"{formlist[i]}"'
            else:
                formlist[i] = f'":{formlist[i]}"'

            last = (False, True)
        else:

            if formlist[i] in '{[(':
                if last[1] or last[0]:
                    formlist[i] = f'+('
                else:
                    formlist[i] = f'('
            else:
                formlist[i] = f')'

            last = (False, False)
    form = ''.join(formlist)
    made_of = eval(form)[1::].split(':')
    return dict(Counter(made_of))


print(parse_molecule('H2O'))
print(parse_molecule('(H2O)'))
print(parse_molecule('Mg(OH)2'))
print(parse_molecule('K4[ON(SO3)2]2'))
print(parse_molecule('C2H5OH'))
