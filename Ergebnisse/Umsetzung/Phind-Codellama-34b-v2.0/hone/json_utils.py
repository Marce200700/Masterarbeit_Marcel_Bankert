import json

def read_json(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)

def write_json(filepath, data, indent=4):
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=indent)

def write_json_stdout(data, indent=4):
    print(json.dumps(data, indent=indent))