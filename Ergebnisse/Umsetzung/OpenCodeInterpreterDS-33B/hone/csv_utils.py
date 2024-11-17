import csv

def read_csv(filepath):
    """
    Reads a CSV file and returns a list of dictionaries, where each dictionary represents a row in the CSV file.
    """
    with open(filepath, 'r') as file:
        reader = csv.DictReader(file)
        data = list(reader)
    return data
