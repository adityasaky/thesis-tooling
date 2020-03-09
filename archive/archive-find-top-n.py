import json
import operator
import sys


if __name__ == "__main__":
    start = 0
    end = sys.argv[1]
    with open(sys.argv[2], "r") as fp:
        pagerank = json.load(fp)

    sorted_pagerank = sorted(pagerank.items(), key=operator.itemgetter(1), reverse=True)

    if "-" in end:
        start, end = end.split("-")

    for i in range(int(start), int(end)):
        print(i + 1, sorted_pagerank[i][0], sorted_pagerank[i][1])

