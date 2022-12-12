from lib.handle_input import read_input
import re

class Monkey:
    def __init__(self, label, inventory, operation, test, iftrue, iffalse):
        self.label = label
        self.inventory = inventory
        self.operation = operation
        self.test = test
        self.iftrue = iftrue
        self.iffalse = iffalse
        self.inspections = 0

    def __str__(self):
        return 'Monkey {} holding {}, throws to {} or {}, inspections {}'.format(
            self.label, self.inventory, self.iftrue, self.iffalse, self.inspections)

    def add_item(self, item):
        self.inventory.append(item)

    def take_turn(self, monkeys):
        for item in self.inventory:
            new_item = self.operation(item)
            self.inspections += 1
            if self.test(new_item):
                monkeys[self.iftrue].add_item(new_item)
            else:
                monkeys[self.iffalse].add_item(new_item)
        self.inventory = []


def format_data(input_data):
    monkeys = input_data.rstrip('\n').split('\n\n')
    return monkeys

def read_monkey(monkey):
    pattern = re.compile(r'Monkey (\d+):\s*'            # 1
        r'Starting items: (\d+(, \d+)*)\s*'             # 2, 3
        r'Operation: new = (\w+) ([+*]) (\w+)\s*'       # 4, 5, 6
        r'Test: divisible by (\d+)\s*'                  # 7
        r'If true: throw to monkey (\d+)\s*'            # 8
        r'If false: throw to monkey (\d+)\s*')          # 9
    matches = pattern.fullmatch(monkey)
    label = int(matches[1])
    inventory = [int(item) for item in matches[2].split(', ')]
    if matches[6] == 'old':
        operation = lambda x: x * x // 3
    else:
        if matches[5] == '*':
            operation = lambda x: (x * int(matches[6])) // 3
        else:
            operation = lambda x: (x + int(matches[6])) // 3
    test = lambda x: x % int(matches[7]) == 0
    iftrue = int(matches[8])
    iffalse = int(matches[9])
    monkey = Monkey(label, inventory, operation, test, iftrue, iffalse)
    return monkey

def part1(data):
    monkeys = [read_monkey(datum) for datum in data]
    for i in range(20):
        for monkey in monkeys:
            monkey.take_turn(monkeys)
    sorted_monkeys = sorted(monkeys, key=lambda monkey: monkey.inspections, reverse=True)
    return sorted_monkeys[0].inspections * sorted_monkeys[1].inspections

def main():
    data = format_data(read_input('data/day11.txt'))
    print('Monkey business: {}'.format(part1(data)))

if __name__ == '__main__':
    main()