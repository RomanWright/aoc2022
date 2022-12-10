from lib.handle_input import read_input

class CycleCounter:
    points_of_interest = [20, 60, 100, 140, 180, 220]
    def __init__(self):
        self.x = 1
        self.cycle = 0
        self.signal_strength = []

    def increment_cycle(self, times):
        for _ in range(times):
            self.cycle += 1
            if self.cycle in self.points_of_interest:
                self.signal_strength.append(self.x * self.cycle)
    
    def noop(self):
        self.increment_cycle(1)

    def addx(self, y):
        self.increment_cycle(2)
        self.x += y

def part1(data):
    tracker = CycleCounter()
    for instruction in data:
        if instruction == 'noop':
            tracker.noop()
        else:
            _, y = instruction.split(' ')
            tracker.addx(int(y))
    return sum(tracker.signal_strength)

def main():
    data = read_input('data/day10.txt').split('\n')
    print('The total signal strength is {}'.format(part1(data)))

if __name__ == '__main__':
    main()