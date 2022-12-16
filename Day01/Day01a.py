if __name__ == '__main__':
    with open('input.data', encoding="utf-8", mode="rt") as f:
        numbers_string  = f.readlines()
    cal_list = list()
    single_elf = list()
    buffer = 0;
    for char in numbers_string:
        if char != '\n':
            number = int(char)
            single_elf.append(number)
            buffer += number
        else:
            single_elf.append(buffer)
            cal_list.append(single_elf)
            single_elf = list()
            buffer = 0
    max = 0
    max_pos = 0
    for pos, Anumber in enumerate(cal_list):
        if Anumber[-1] > max:
            max = Anumber[-1]
            max_pos = pos
    print(cal_list)
    print(max_pos, max)



