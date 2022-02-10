def pets(years):
    one = 15
    two = 24
    dog = 5*(years-2)+24
    cat = 4*(years-2)+24
    if years == 1:
        return [years, 15, 15]
    elif years == 2:
        return [years, 24, 24]
    elif years >=3:
        return [years, cat, dog]
    else:
        return [0, 0, 0]

