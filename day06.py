from lib.handle_input import read_input

def part1():
    data = read_input('data/day06.txt')
    return find_marker(data, 4)

def find_marker(data, marker_length):
    index = 0
    while index <= len(data) - marker_length:
        test = set(data[index:index+marker_length])
        if len(test) == marker_length:
            return index + marker_length
        index += 1
    return None

def part2():
    data = read_input('data/day06.txt')
    return find_marker(data, 14)

def main():
    print('The packet marker ends at {}'.format(part1()))
    print('The message marker ends at {}'.format(part2()))

if __name__ == '__main__':
    main()