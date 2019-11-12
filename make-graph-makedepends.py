import os
import networkx as nx
import sys
import json
import requests
import time


DATA_ROOT = "data"
GRAPH_ROOT = "graphs"
PAGERANK_ROOT = "pagerank"


def make_graph(data):
    graph = nx.DiGraph()

    for package in data:
        graph.add_node(package)
        for makedepend in data.get(package):
            graph.add_node(makedepend)
            graph.add_edge(package, makedepend)

    return graph


if __name__ == "__main__":
    if len(sys.argv) < 2:
        data_file_name = "packages_makedepends_2019-11-12.json"
    else:
        data_file_name = sys.argv[1]

    data_path = os.path.join(DATA_ROOT, data_file_name)

    print("Loading {}...".format(data_file_name))
    with open(data_path, "r") as data_fp:
        data = json.load(data_fp)

    print("Making graph...")
    graph = make_graph(data)

    print("Calculating PageRank...")
    pagerank = nx.pagerank(graph)

    with open(os.path.join(PAGERANK_ROOT, "pagerank_" + data_file_name), "w+") as fp:
        json.dump(pagerank, fp)

