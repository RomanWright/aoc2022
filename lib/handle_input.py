def read_input(filepath):
    with open(filepath, encoding="utf-8") as f:
        data = f.read().rstrip('\n').split('\n\n')
    return [datum.split('\n') for datum in data]