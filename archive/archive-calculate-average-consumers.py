import json
import sys


if __name__ == "__main__":
    data_file_path = sys.argv[1]

    with open(data_file_path) as fp:
        data = json.load(fp)

    all_packages = set()
    total_consumption = 0

    for package in data:
        all_packages.add(package)
        total_consumption += len(data[package])
        for consumer in data[package]:
            all_packages.add(consumer)

    total_packages = len(all_packages)

    print("Average consumption: ", total_consumption / total_packages)
