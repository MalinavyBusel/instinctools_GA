def IP(ip):
    total_sum = ''
    parts = ip.split(ip[4])
    for part in parts:
        summed = 0
        for elem in part:
            summed += int(elem, 16)
        total_sum += str(summed)
    return total_sum


print(IP('1B1D:AF01:3847:F8C4:20E9:0111:DFEA:AAAA'))
