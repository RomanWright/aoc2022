from lib.handle_input import read_input

def part1(data):
    head = [0, 0]
    tail = [0, 0]
    tail_set = set()
    tail_set.add(stringify_position(tail))
    for instruction in data:
        execute_instruction(instruction, head, tail, tail_set)
    return len(tail_set)

def execute_instruction(instruction, head, tail, tail_set):
    direction, distance = instruction.split(' ')
    if direction == 'R':
        for _ in range(int(distance)):
            execute_step((1, 0), head, tail)
            tail_set.add(stringify_position(tail))
    if direction == 'L':
        for _ in range(int(distance)):
            execute_step((-1, 0), head, tail)
            tail_set.add(stringify_position(tail))
    if direction == 'U':
        for _ in range(int(distance)):
            execute_step((0, 1), head, tail)
            tail_set.add(stringify_position(tail))
    if direction == 'D':
        for _ in range(int(distance)):
            execute_step((0, -1), head, tail)
            tail_set.add(stringify_position(tail))

def execute_step(step, head, tail):
    head[0] += step[0]
    head[1] += step[1]
    distance = abs(head[0] - tail[0]) + abs(head[1] - tail[1])
    if distance == 2:
        if head[0] == tail[0]:
            tail[1] = (head[1] + tail[1]) / 2
        elif head[1] == tail[1]:
            tail[0] = (head[0] + tail[0]) / 2
    elif distance == 3:
        vector = [head[0] - tail[0], head[1] - tail[1]]
        if vector[0] == 2:
            vector[0] = 1
        elif vector[0] == -2:
            vector[0] = -1
        elif vector[1] == 2:
            vector[1] = 1
        elif vector[1] == -2:
            vector[1] = -1
        tail[0] += vector[0]
        tail[1] += vector[1]

def stringify_position(tail):
    return '{}x{}y'.format(tail[0], tail[1])

def main():
    data = read_input('data/day09.txt').split('\n')
    print('The total positions the tail moves to is {}'.format(part1(data)))

if __name__ == '__main__':
    main()