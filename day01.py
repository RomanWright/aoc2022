from lib.handle_input import read_input

def format_data(input_data):
    data = input_data.rstrip('\n').split('\n\n')
    return [datum.split('\n') for datum in data]

def generate_calorie_list():
    elves = format_data(read_input('data/day01.txt'))
    calories = [[int(item) for item in elf] for elf in elves]
    return [sum(items) for items in calories]

def part1():
    total_calories = generate_calorie_list()
    return max(total_calories)

def part2():
    total_calories = generate_calorie_list()
    total_calories.sort(reverse=True)
    top_three = total_calories[:3]
    return sum(top_three)

def main():
    print('The most calories an Elf is carrying is {}'.format(part1()))
    print('The calories carried by the three elves totals {}'.format(part2()))

if __name__ == '__main__':
    main()