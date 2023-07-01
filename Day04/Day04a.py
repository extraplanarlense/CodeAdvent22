import re


def removeElements(A, B):
    n = len(A)
    return any(A == B[i:i + n] for i in range(len(B)-n + 1))

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
            if removeElements(rangeA, rangeB):
                contains += 1
        else:
            if removeElements(rangeB, rangeA):
                contains += 1
    print(contains)
    print(count)
