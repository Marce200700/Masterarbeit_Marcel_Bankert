import json

def write_json(data, filepath=None):
    """
    Writes a JSON structure to a file or standard output.
    """
    if filepath:
        with open(filepath, 'w') as file:
            json.dump(data, file, indent=4, sort_keys=True)
    else:
        print(json.dumps(data, indent=4, sort_keys=True))