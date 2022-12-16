if __name__ == '__main__':
    with open('input.data', encoding="utf-8", mode="rt") as f:
        rucksack_list = f.readlines()
    counter = 0
    points = 0
    for rucksack_number in range(0, len(rucksack_list), 3):
        rucksack1 = rucksack_list[rucksack_number]
        r1 = rucksack1.strip()
        rucksack2 = rucksack_list[rucksack_number+1]
        r2 = rucksack2.strip()
        rucksack3 = rucksack_list[rucksack_number+2]
        r3 = rucksack3.strip()
        same1and2 = ''.join(set(r1).intersection(r2))
        same2and3 = ''.join(set(same1and2).intersection(r3))
        priority = ord(same2and3)
        if priority > 90:
            points += priority - 96
        else:
            points += priority - 38
    print(points)