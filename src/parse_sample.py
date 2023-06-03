def parse_sample(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    values = [float(line) for line in lines[:-1]]
    return values