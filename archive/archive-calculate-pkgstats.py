"""
This file calculates the popularity metric and dumps it to data/
"""

import requests
import time
import sys
import os
import json


DATA_ROOT = "data"
PERSONALIZATION_ROOT = "personalization"


def list_all_packages(data):
    all_packages = []

    for package in data:
        all_packages.append(package)
        all_packages.extend(data[package])

    return list(set(all_packages))


def calculate_and_dump_weights(data, data_file_name):

    def _dump_weights():
        with open(pkgstats_path, "w") as fp:
            json.dump(weights, fp)

    pkgstats_path = os.path.join(DATA_ROOT, "pkgstats_" + data_file_name)
    url = "https://pkgstats.archlinux.de/api/packages/{}"

    all_packages = list_all_packages(data)

    if os.path.exists(pkgstats_path):
        with open(pkgstats_path) as fp:
            weights = json.load(fp)
    else:
        weights = {}

    failure = []

    i = 0
    for package in all_packages:
        if package in weights:
            continue
        response = requests.get(url.format(package))
        try:
            weights[package] = json.loads(response.content)["popularity"]
        except json.decoder.JSONDecodeError:
            failure.append(package)
            weights[package] = 0.001
        i += 1
        if i % 75 == 0:
            _dump_weights()
            time.sleep(1)

    print(failure)

    _dump_weights()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        data_file_name = "data_2019-11-27_pkg.json"
    else:
        data_file_name = sys.argv[1]

    data_path = os.path.join(DATA_ROOT, data_file_name)

    print("Loading {}...".format(data_file_name))
    with open(data_path, "r") as data_fp:
        data = json.load(data_fp)

    calculate_and_dump_weights(data, data_file_name)
