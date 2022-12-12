from lib.handle_input import read_input

alphabet = 'abcdefghijklmnopqrstuvwxyz'

class Position:
    def __init__(self, x, y, heightmap, positionmap):
        self.x = x
        self.y = y
        self.height = self.height(heightmap)
        self.positionmap = positionmap
        self.cost = None
    
    def __str__(self):
        return '({}, {}), {} height, {} steps from the end'.format(self.x, self.y, alphabet[self.height], self.cost)

    def height(self, heightmap):
        if heightmap[self.y][self.x] in alphabet:
            return alphabet.find(heightmap[self.y][self.x])
        if heightmap[self.y][self.x] == 'S':
            return 0
        if heightmap[self.y][self.x] == 'E':
            return 25
        return None

    def find_neighbors(self):
        neighbors = []
        if self.x > 0:
            neighbors.append(self.positionmap[self.y][self.x-1])
        if self.y > 0:
            neighbors.append(self.positionmap[self.y-1][self.x])
        if self.x < len(self.positionmap[self.y]) - 1:
            neighbors.append(self.positionmap[self.y][self.x+1])
        if self.y < len(self.positionmap) - 1:
            neighbors.append(self.positionmap[self.y+1][self.x])
        return neighbors

    def find_walkable_neighbors(self):
        walkable_neighbors = []
        for neighbor in self.find_neighbors():
            if neighbor.height >= self.height - 1:
                walkable_neighbors.append(neighbor)
        return walkable_neighbors

def part1(data):
    positionmap = []
    start = None
    end = None
    for i in range(len(data)):
        rowmap = []
        for j in range(len(data[i])):
            position = Position(j, i, data, positionmap)
            rowmap.append(position)
            if data[i][j] == 'S':
                start = position
            if data[i][j] == 'E':
                end = position
        positionmap.append(rowmap)
    end.cost = 0
    fringe = [end]
    while len(fringe) > 0:
        current = fringe.pop(0)
        for neighbor in current.find_walkable_neighbors():
            if (not neighbor.cost) or (neighbor.cost > current.cost + 1):
                neighbor.cost = current.cost + 1
                fringe.append(neighbor)
    return start.cost

def part2(data):
    positionmap = []
    end = None
    for i in range(len(data)):
        rowmap = []
        for j in range(len(data[i])):
            position = Position(j, i, data, positionmap)
            rowmap.append(position)
            if data[i][j] == 'S':
                start = position
            if data[i][j] == 'E':
                end = position
        positionmap.append(rowmap)
    end.cost = 0
    fringe = [end]
    while len(fringe) > 0:
        current = fringe.pop(0)
        for neighbor in current.find_walkable_neighbors():
            if (not neighbor.cost) or (neighbor.cost > current.cost + 1):
                neighbor.cost = current.cost + 1
                fringe.append(neighbor)
    flat_map = [position for row in positionmap for position in row]
    a_heights = [position for position in flat_map if position.height == 0 and position.cost]
    a_heights.sort(key=lambda position: position.cost)
    return a_heights[0].cost

def main():
    data = read_input('data/day12.txt').split('\n')
    print('Steps: {}'.format(part1(data)))
    print('Fewest steps: {}'.format(part2(data)))

if __name__ == '__main__':
    main()