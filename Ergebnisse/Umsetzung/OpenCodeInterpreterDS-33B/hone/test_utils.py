import json
import csv

def parse_json(filepath):
    """
    Parses a JSON file and returns the JSON structure.
    """
    with open(filepath, 'r') as file:
        data = json.load(file)
    return data

def parse_csv(filepath):
    """
    Parses a CSV file and returns a list of dictionaries, where each dictionary represents a row in the CSV file.
    """
    with open(filepath, 'r') as file:
        reader = csv.DictReader(file)
        data = list(reader)
    return data