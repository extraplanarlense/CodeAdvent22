import re


def check_list_contained(A, B):
    # convert list A to string
    A_str = ' '.join(map(str, A))
    # convert list B to string
    B_str = ' '.join(map(str, B))
    # find all instances of A within B
    instances = re.findall(A_str, B_str)

    # return True if any instances were found, False otherwise
    return len(instances) > 0

if __name__ == '__main__':
    with open('input.data', encoding="utf-8", mode="rt") as f:
        section_list = f.readlines()
    contains = 0
    count = 0
    for section in section_list:
        section = section.strip()
        section = section.split(',')
        [rangeAstart, rangeAend] = section[0].split('-')
        [rangeBstart, rangeBend] = section[1].split('-')
        rangeA = list(range(int(rangeAstart), int(rangeAend)+1))
        rangeB = list(range(int(rangeBstart), int(rangeBend)+1))
        if len(rangeB) > len(rangeA):
            if check_list_contained(rangeA, rangeB) == False:
                contains += 1
        else:
            if check_list_contained(rangeB, rangeA) == False:
                contains += 1



    print(contains)
    print(count)
