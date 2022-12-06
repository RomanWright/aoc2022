from lib.handle_input import read_input

def part1():
    data = read_input('data/day06.txt')
    index = 0
    while index < len(data) - 3:
        test = set(data[index:index+4])
        if len(test) == 4:
            return index + 4
        index += 1
    return None

def main():
    print('The first marker ends at {}'.format(part1()))

if __name__ == '__main__':
    main()