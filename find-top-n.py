import json
import operator
import sys


if __name__ == "__main__":
    count = int(sys.argv[1])
    with open(sys.argv[2], "r") as fp:
        pagerank = json.load(fp)

    sorted_pagerank = sorted(pagerank.items(), key=operator.itemgetter(1), reverse=True)

    for i in range(count):
        print(sorted_pagerank[i])

