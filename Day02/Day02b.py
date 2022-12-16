if __name__ == '__main__':
    with open('input.data', encoding="utf-8", mode="rt") as f:
        pair_list = f.readlines()
    points = 0
    for pair in pair_list:
        if pair[0] == 'A':
            if pair[2] == 'X':
                points += 3  # 1 + 3
            if pair[2] == 'Y':
                points += 4  # 2 + 6
            if pair[2] == 'Z':
                points += 8  # 3 + 0
        if pair[0] == 'B':
            if pair[2] == 'X':
                points += 1  # 1 + 0
            if pair[2] == 'Y':
                points += 5  # 2 + 3
            if pair[2] == 'Z':
                points += 9  # 3 + 6
        if pair[0] == 'C':
            if pair[2] == 'X':
                points += 2  # 1 + 6
            if pair[2] == 'Y':
                points += 6  # 2 + 0
            if pair[2] == 'Z':
                points += 7  # 3 + 3
    print(points)
