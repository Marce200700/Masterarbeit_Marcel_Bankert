import csv

def read_csv(filepath, delimiter=','):
    with open(filepath, 'r') as file:
        reader = csv.reader(file, delimiter=delimiter)
        return list(reader)

def write_csv(filepath, data, delimiter=','):
    with open(filepath, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=delimiter)
        writer.writerows(data)