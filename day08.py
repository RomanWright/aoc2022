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
    visible = visible or is_tallest(height, data[x][:y])
    visible = visible or is_tallest(height, data[x][y+1:])
    visible = visible or is_tallest(height, [datum[y] for datum in data[:x]])
    visible = visible or is_tallest(height, [datum[y] for datum in data[x+1:]])
    return visible

def is_tallest(height, others):
    if len(others) == 0:
        return True
    elif max(others) < height:
        return True
    return False

def part2(data):
    best_score = 0
    for x in range(len(data)):
        for y in range(len(data[x])):
            if scenic_score(data, x, y) > best_score:
                best_score = scenic_score(data, x, y)
    return best_score

def scenic_score(data, x, y):
    height = data[x][y]

    score1 = 0
    testx, testy = x, y - 1
    while testy >= 0 and data[testx][testy] <= height:
        score1 += 1
        if data[testx][testy] == height:
            break
        testy -= 1

    score2 = 0
    testx, testy = x, y + 1
    while testy < len(data[testx]) and data[testx][testy] <= height:
        score2 += 1
        if data[testx][testy] == height:
            break
        testy += 1
    
    score3 = 0
    testx, testy = x - 1, y
    while testx >= 0 and data[testx][testy] <= height :
        score3 += 1
        if data[testx][testy] == height:
            break
        testx -= 1

    score4 = 0
    testx, testy = x + 1, y
    while testx < len(data) and data[testx][testy] <= height:
        score4 += 1
        if data[testx][testy] == height:
            break
        testx += 1
    return score1 * score2 * score3 * score4

def main():
    data = read_input('data/day08.txt').split('\n')
    print('There are {} visible trees'.format(part1(data)))
    print('The highest scenic score is {}'.format(part2(data)))

if __name__ == '__main__':
    main()