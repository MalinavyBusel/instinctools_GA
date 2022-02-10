def height(classmates, vovochka):
    classmates.append(vovochka)
    classmates = sorted(classmates)
    classmates.reverse()
    position = classmates.index(vovochka) + classmates.count(vovochka)
    print(classmates)
    return position

# !!! Нумерация начинается с единицы !!!
print(height([204, 105, 210, 231], 195))
