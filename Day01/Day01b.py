if __name__ == '__main__':
    with open('input.data', encoding="utf-8", mode="rt") as f:
        numbers_string  = f.readlines()
    cal_list = list()
    single_elf_cal = list()
    buffer = 0;
    for line in numbers_string:
        if line != '\n':
            number = int(line)
            buffer += number
        else:
            single_elf_cal.append(buffer)
            buffer = 0
        single_elf_cal.sort()
    print(single_elf_cal)
    print("Max 3 Calories:", sum(single_elf_cal[-3:]))


