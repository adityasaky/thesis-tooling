import json
import sys
import operator


if __name__ == "__main__":
    package = sys.argv[1]
    with open(sys.argv[2], "r") as fp:
        pagerank = json.load(fp)

    sorted_pagerank = sorted(pagerank.items(), key=operator.itemgetter(1), reverse=True)

    for i in range(len(sorted_pagerank)):
        if sorted_pagerank[i][0] == package:
            print(i + 1, sorted_pagerank[i][0], sorted_pagerank[i][1])
            break

