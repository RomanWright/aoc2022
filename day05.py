from lib.handle_input import read_input
import re

class Tower:
    def __init__(self, label):
        self.label = label
        self.stack = []
    
    def add(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def move(self, other_tower):
        other_tower.add(self.pop())

    def __str__(self):
        return 'Tower {} containing stack {}'.format(self.label, str(self.stack))

def part1():
    columns, procedure = read_input('data/day05.txt').split('\n\n')
    instructions = procedure.split('\n')
    towers = read_columns(columns)
    for instruction in instructions:
        execute_instruction(towers, instruction)
    return "".join([tower.peek() for tower in towers.values()])

def read_columns(columns):
    rows = columns.split('\n')
    labels = [int(item) for item in rows.pop().split()]
    towers = {}
    for label in labels:
        towers[label] = Tower(label)
    while len(rows) > 0:
        next_row = rows.pop()
        tower_index = 1
        while len(next_row) > 0:
            crate, next_row = next_row[1], next_row[4:]
            if crate != ' ':
                towers[tower_index].add(crate)
            tower_index += 1
    return towers

def execute_instruction(towers, instruction):
    count, from_tower, to_tower = read_instruction(instruction)
    for _ in range(count):
        towers[from_tower].move(towers[to_tower])

def read_instruction(instruction):
    pattern = re.compile(r'move (\d+) from (\d+) to (\d+)')
    matches = pattern.fullmatch(instruction)
    return int(matches[1]), int(matches[2]), int(matches[3])


def main():
    print('The top crates are {}'.format(part1()))

if __name__ == '__main__':
    main()