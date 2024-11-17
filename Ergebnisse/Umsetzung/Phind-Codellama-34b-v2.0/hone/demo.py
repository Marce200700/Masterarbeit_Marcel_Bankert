import argparse
from hone import Hone

def main():
    parser = argparse.ArgumentParser(description='Convert CSV to JSON using Hone.')
    parser.add_argument('csv_filepath', type=str, help='Path to the input CSV file.')
    parser.add_argument('json_filepath', type=str, help='Path to the output JSON file.')
    args = parser.parse_args()

    hone = Hone()
    json_data = hone.convert(args.csv_filepath)

    with open(args.json_filepath, 'w') as json_file:
        json.dump(json_data, json_file, indent=4, sort_keys=True)

if __name__ == '__main__':
    main()