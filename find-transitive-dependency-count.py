import os
import json


DATA_ROOT = "data"
LOG_ROOT = "log"


def main():
    data_file_name = "data_2019-10-24_pkg.json"
    data_file_path = os.path.join(DATA_ROOT, data_file_name)

    output_file_path = os.path.join(DATA_ROOT, "transitive_count_" + data_file_name)

    completed_dependencies_log_path = os.path.join(LOG_ROOT, data_file_name)

    try:
        with open(output_file_path) as fp:
            counter = json.load(fp)
    except:
        counter = {}

    try:
        with open(completed_dependencies_log_path) as fp:
            completed_dependencies = json.load(fp)
    except:
        completed_dependencies = []

    with open(data_file_path) as fp:
        data = json.load(fp)

    for dependency in data:
        if dependency in completed_dependencies:
            continue
        for consumer in data.get(dependency):
            if consumer in counter:
                counter[consumer] += 1
            else:
                counter[consumer] = 1
        completed_dependencies.append(dependency)
        with open(completed_dependencies_log_path, "w+") as fp:
            json.dump(completed_dependencies, fp)
        with open(output_file_path, "w+") as fp:
            json.dump(counter, fp)


if __name__ == "__main__":
    main()
