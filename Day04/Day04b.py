import re


def removeElements(A, B):
    n = len(A)
    return any(A == B[i:i + n] for i in range(len(B)-n + 1))

if __name__ == '__main__':
    with open('input.data', encoding="utf-8", mode="rt") as f:
        section_list = f.readlines()
    overlap = 0
    for section in section_list:
        print(section)
        section = section.strip()
        section = section.split(',')
        [rangeAstart, rangeAend] = section[0].split('-')
        [rangeBstart, rangeBend] = section[1].split('-')
        #print("!!!", overlap, rangeAstart, rangeAend, rangeBstart, rangeBend)
        #print((rangeAstart <= rangeBstart <= rangeAend), rangeBstart <= rangeAstart <= rangeBend)
        if ((rangeAstart <= rangeBstart <= rangeAend) or (rangeBstart <= rangeAstart <= rangeBend)):
            overlap += 1
            #print("###", rangeAstart, rangeAend, rangeBstart, rangeBend)
    print(overlap)
