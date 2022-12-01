from lib.handle_input import read_input
import pdb

def part1():
    elves = read_input('data/day01.txt')
    calories = [[int(item) for item in elf] for elf in elves]
    total_calories = [sum(items) for items in calories]
    return max(total_calories)

def main():
    print(part1())

if __name__ == '__main__':
    main()