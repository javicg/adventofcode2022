from csv import reader


def solve(input_file: str) -> str:
    # Read input
    cache = {}
    with open(input_file, 'r') as read_obj:
        csv_reader = reader(read_obj)
        for row in csv_reader:
            cache[row[0]] = row[1]

    # Process input

    # Print output
    return cache['5']


if __name__ == '__main__':
    print(solve("resources/problem1.csv"))
