from lib.handle_input import read_input

def part1(data):
    total_visible = 0
    for x in range(len(data)):
        for y in range(len(data[x])):
            if is_visible(data, x, y):
                total_visible += 1
    return total_visible

def is_visible(data, x, y):
    visible = False
    height = data[x][y]
    # Left
    visible = visible or is_tallest(height, data[x][:y])
    # Right
    visible = visible or is_tallest(height, data[x][y+1:])
    # Top
    visible = visible or is_tallest(height, [datum[y] for datum in data[:x]])
    # Bottom
    visible = visible or is_tallest(height, [datum[y] for datum in data[x+1:]])
    return visible

def is_tallest(height, others):
    if len(others) == 0:
        return True
    elif max(others) < height:
        return True
    return False

def main():
    data = read_input('data/day08.txt').split('\n')
    print('There are {} visible trees'.format(part1(data)))

if __name__ == '__main__':
    main()