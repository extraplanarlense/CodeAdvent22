if __name__ == '__main__':
    with open('input.data', encoding="utf-8", mode="rt") as f:
        rucksack_list = f.readlines()
    points = 0
    for rucksack in rucksack_list:
        firstpart, secondpart = rucksack[:len(rucksack) // 2], rucksack[len(rucksack) // 2:]
        common = ''.join(set(firstpart).intersection(secondpart))
        priority = ord(common)
        if priority > 90:
            points += priority - 96
        else:
            points += priority - 38
    print(points)