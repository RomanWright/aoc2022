def read_input(filepath):
    with open(filepath, encoding="utf-8") as f:
        data = f.read()
    return data

def format_data(input_data):
    return input_data.rstrip('\n').split('\n')