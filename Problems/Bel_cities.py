txt = 'Minsk ibh KHlgs grODno lslnn Vitebsk'


def cities(city_str):
    my_cities = {'brest': 1, 'grodno': 1, 'gomel': 1, 'mogilev': 1, 'vitebsk': 1, 'minsk': 1, }
    lst = []
    input_list = city_str.split()
    for elem in input_list:
        if my_cities.setdefault(elem.lower(), 0):
            lst.append(elem)
    return lst


print(cities(txt))
