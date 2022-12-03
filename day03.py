from lib.handle_input import read_input

def format_data(input_data):
    return input_data.rstrip('\n').split('\n')

def prioritize(letter):
    priorities = '0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return priorities.index(letter)

def part1():
    rucksacks = format_data(read_input('data/day03.txt'))
    total_priority = 0
    for rucksack in rucksacks:
        compartment1 = set(rucksack[:len(rucksack) // 2])
        compartment2 = set(rucksack[len(rucksack) // 2:])
        shared = compartment1.intersection(compartment2)
        total_priority += prioritize(shared.pop())
    return total_priority

def part2():
    rucksacks = format_data(read_input('data/day03.txt'))
    i = 0
    total_priority = 0
    while i < len(rucksacks):
        member1 = set(rucksacks[i])
        member2 = set(rucksacks[i + 1])
        member3 = set(rucksacks[i + 2])
        shared = member1.intersection(member2, member3)
        total_priority += prioritize(shared.pop())
        i += 3
    return total_priority

def main():
    print('The total priority of each rucksack is {}'.format(part1()))
    print('The total priority of each group is {}'.format(part2()))

if __name__ == '__main__':
    main()