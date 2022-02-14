def height(classmates):
    boy = int(input('The age of Vova is: '))
    classmates.append(boy)
    classmates = sorted(classmates)
    classmates.reverse()

    # !!! Enumeration starts with 1 !!!
    position = classmates.index(boy) + classmates.count(boy)
    print(classmates)
    return position


if __name__ == '__main__':
    print(height([204, 105, 210, 231]))
