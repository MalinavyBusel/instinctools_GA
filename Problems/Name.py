def name(initials):
    parts = initials.split()
    for j in range(len(parts)):
        for i in range(len(parts[j])):
            if not (parts[j][i].isalpha()):
                parts[j] = parts[j][:i].title()
                break
    for i in range(3):
        print(parts[i])


if __name__ == '__main__':
    name('egor8479 VsLJHch*^ie Bgtrvch35633')
