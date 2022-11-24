from csv import reader

INPUT_FILE = "resources/problem1.csv"

if __name__ == '__main__':
    # Read input
    cache = {}
    with open(INPUT_FILE, 'r') as read_obj:
        csv_reader = reader(read_obj)
        for row in csv_reader:
            cache[row[0]] = row[1]

    # Process input

    # Print output
    print(cache['5'])
