def name(initials):
    parts = initials.split()
    for j in range(len(parts)):
        for i in range(len(parts[j])):
            if not (parts[j][i].isupper() or parts[j][i].islower()):
                parts[j] = parts[j][:i].title()
                break
    for i in range(3):
        print(parts[i])


name('egor8479 VsLJHch*^ie Bgtrvch35633')