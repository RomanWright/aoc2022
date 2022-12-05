from lib.handle_input import read_input, format_data
import pdb

class Pair:
    def __init__(self, f1, f2, s1, s2):
        self.f1 = f1
        self.f2 = f2
        self.s1 = s1
        self.s2 = s2

def read_line(pair_string):
    first, second = pair_string.split(',')
    f1, f2 = first.split('-')
    s1, s2 = second.split('-')
    return Pair(int(f1), int(f2), int(s1), int(s2))

def is_contained(pair):
    if pair.f1 <= pair.s1 and pair.f2 >= pair.s2:
        return True
    if pair.s1 <= pair.f1 and pair.s2 >= pair.f2:
        return True
    return False

def part1():
    pairs = format_data(read_input('data/day04.txt'))
    return [is_contained(read_line(pair)) for pair in pairs].count(True)

def overlaps(pair):
    if is_contained(pair):
        return True
    if pair.f1 <= pair.s1 and pair.f2 >= pair.s1:
        return True
    if pair.s1 <= pair.f1 and pair.s2 >= pair.f1:
        return True
    return False

def part2():
    pairs = format_data(read_input('data/day04.txt'))
    return [overlaps(read_line(pair)) for pair in pairs].count(True)

def main():
    print('There are {} totally contained pairs'.format(part1()))
    print('There are {} overlapping pairs'.format(part2()))

if __name__ == '__main__':
    main()