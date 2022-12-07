from lib.handle_input import read_input

class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.subdirectories = {}
        self.files = {}
    
    def add_file(self, filename, filesize):
        self.files[filename] = filesize
    
    def add_subdirectory(self, name, child):
        self.subdirectories[name] = child

    def immediate_size(self):
        return sum(self.files.values())

    def total_size(self):
        return self.immediate_size() + sum([subdirectory.total_size() for subdirectory in self.subdirectories.values()])

    def __str__(self):
        return 'Directory {} containing subdirectories {} and files {}'.format(
            self.name, self.subdirectories.keys(), self.files.keys()
        )

root = Directory("/", None)
root.parent = root

def part1(data):
    command_responses = map(lambda x: x.strip(), data.split('$'))
    assemble_tree(command_responses)
    sum_folder_sizes = 0
    for node in traverse(root):
        if node.total_size() <= 100000:
            sum_folder_sizes += node.total_size()
    return sum_folder_sizes

def assemble_tree(command_responses):
    node = None
    for command_response in command_responses:
        if command_response == "":
            pass
        elif command_response == "cd /":
            node = root
        elif command_response == "cd ..":
            node = node.parent
        elif command_response[0:2] == "cd":
            node = node.subdirectories[command_response[3:]]
        elif command_response[0:2] == "ls":
            handle_ls(node, command_response[3:])
            
def handle_ls(current_node, response):
    elements = response.split('\n')
    for element in elements:
        if element[0:3] == "dir":
            current_node.add_subdirectory(element[4:], Directory(element[4:], current_node))
        else:
            size, name = element.split(' ')
            current_node.add_file(name, int(size))

def traverse(start):
    node = start
    fringe = [node]
    while len(fringe) != 0:
        node = fringe.pop(0)
        fringe.extend(node.subdirectories.values())
        yield node
    return None


def main():
    data = read_input('data/day07.txt')
    print('The folders with small size total {}'.format(part1(data)))

if __name__ == '__main__':
    main()