from hone import Hone

def main():
    """
    Demonstration of the Hone tool's functionality.
    """
    csv_filepath = 'examples/example_a.csv'
    json_filepath = 'examples/example_a.json'

    hone = Hone(csv_filepath)
    hone.convert(json_filepath)

    schema = hone.get_schema()
    print(schema)

if __name__ == '__main__':
    main()