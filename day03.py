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


def main():
    print('The total priority is {}'.format(part1()))

if __name__ == '__main__':
    main()