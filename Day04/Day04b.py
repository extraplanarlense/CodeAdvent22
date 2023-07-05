import re


def remove_elements(A, B):
    n = len(A)
    return any(A == B[i:i + n] for i in range(len(B)-n + 1))

if __name__ == '__main__':
    with open('input.data', encoding="utf-8", mode="rt") as f:
        section_list = f.readlines()
    overlap = 0
    for section in section_list:
        section = section.strip()
        section_a, section_b = section.split(',')
        #print(repr(section_a))
        [range_a_start, range_a_end], [range_b_start, range_b_end] = map(int, section_a.split('-')), map(int, section_b.split('-'))
        #print(repr(range_b_start))
        if (range_a_start <= range_b_start <= range_a_end) or (range_b_start <= range_a_start <= range_b_end):
            overlap += 1
    print(overlap)
