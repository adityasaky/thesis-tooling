import sys
import json


if __name__ == "__main__":
    data_file = sys.argv[1]

    count = 0
    total = 0

    with open(data_file) as fp:
        data = json.load(fp)

    for package in data:
        if data[package]['explicit_dependencies'] == 0:
            count += 1
            continue
        total += (data[package]['transitive_dependencies'] / data[package]['explicit_dependencies'])

    print("Average ratio:")
    print(total / (len(data) - count))
