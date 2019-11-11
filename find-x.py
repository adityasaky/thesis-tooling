import json
import sys


if __name__ == "__main__":
    package = sys.argv[1]
    with open(sys.argv[2], "r") as fp:
        pagerank = json.load(fp)

    print(pagerank[package])

