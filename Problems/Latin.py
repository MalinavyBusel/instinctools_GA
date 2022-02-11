def latin(quote):
    parted = quote.rpartition(' ')
    parts = [parted[0].capitalize(), parted[2].capitalize(), ]
    return ' '.join(parts)


if __name__ == '__main__':
    print(latin('Carum eSt qUoD  Rarum EST'))
