def sum_numbers_from_file(filepath):
    total = 0.0
    with open(filepath, 'r') as file:
        for line in file:
            line = line.strip()
            if line:  # skip empty lines
                total += float(line)
    return total
sum_numbers_from_file('non_existent_file.txt')