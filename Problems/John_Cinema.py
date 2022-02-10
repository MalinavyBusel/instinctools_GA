from math import ceil


def john(card, ticket, perc, n=1, t_in_time=1, total=0):
    by_one = n*ticket
    if n == 1:
        t_in_time = ticket*perc
        total = card+t_in_time
    else:
        t_in_time = t_in_time*perc
        total += t_in_time

    if ceil(total) < by_one:
        return n
    else:
        return john(card, ticket, perc, n+1, t_in_time, total)


print(john(500, 15, 0.9))
print(john(100, 10, 0.95))
