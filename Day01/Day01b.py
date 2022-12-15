if __name__ == '__main__':
    with open('input.data') as f:
        numbers_string  = f.readlines()
    cal_list = list()
    single_elf_cal = list()
    buffer = 0;
    for char in numbers_string:
        if char != '\n':
            number = int(char)
            buffer += number
        else:
            single_elf_cal.append(buffer)
            buffer = 0
        single_elf_cal.sort()
    print(single_elf_cal)
    print("Max 3 Calories:", sum(single_elf_cal[-3:]))


