def years_diff(date1, date2):
    year1 = int(date1[:4])
    year2 = int(date2[:4])
    return abs(year1-year2)


print(years_diff('2001/14/11', '2022/10/02'))
