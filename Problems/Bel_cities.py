txt = 'Minsk ibh KHlgs grODno lslnn Vitebssk'


def cities(city_str):
    my_cities = {'brest', 'grodno', 'gomel', 'mogilev', 'vitebsk', 'minsk', }
    lst = []
    input_list = city_str.split()
    for elem in input_list:
        if elem.lower() in my_cities:
            lst.append(elem)
    return lst


if __name__ == '__main__':
    print(cities(txt))
