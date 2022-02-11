def height(classmates):
    vovochka = int(input('Возраст Вовы равен: '))
    classmates.append(vovochka)
    classmates = sorted(classmates)
    classmates.reverse()

    # !!! Нумерация начинается с единицы !!!
    position = classmates.index(vovochka) + classmates.count(vovochka)
    print(classmates)
    return position


if __name__ == '__main__':
    print(height([204, 105, 210, 231]))
