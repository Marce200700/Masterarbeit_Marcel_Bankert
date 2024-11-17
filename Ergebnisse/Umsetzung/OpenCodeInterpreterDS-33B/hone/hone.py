from .utils.csv_utils import read_csv
from .utils.json_utils import write_json

class Hone:
    """
    The Hone class is responsible for converting CSV files to a nested JSON structure.
    """
    def __init__(self, csv_filepath):
        self.csv_filepath = csv_filepath

    def convert(self, json_filepath=None):
        """
        Converts a CSV file to a nested JSON structure and writes the JSON to a file or standard output.
        """
        data = read_csv(self.csv_filepath)
        write_json(data, json_filepath)

    def get_schema(self):
        """
        Retrieves a generated JSON schema based on the structure of the CSV file.
        """
        data = read_csv(self.csv_filepath)
        schema = {}
        for key in data[0].keys():
            schema[key] = type(data[0][key]).__name__
        return schema