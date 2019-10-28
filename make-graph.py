import os
import networkx as nx
import sys
import json
import pydot
import requests
import time


DATA_ROOT = "data"
GRAPH_ROOT = "graphs"
PAGERANK_ROOT = "pagerank"
PERSONALIZATION_ROOT = "personalization"


def make_graph(data):
    graph = nx.DiGraph()

    for required_package in data:
        graph.add_node(required_package)
        for consuming_package in data.get(required_package):
            graph.add_node(consuming_package)
            graph.add_edge(consuming_package, required_package)

    return graph


if __name__ == "__main__":
    if len(sys.argv) < 2:
        data_file_name = "data_2019-10-22_pkg.json"
    else:
        data_file_name = sys.argv[1]

    data_path = os.path.join(DATA_ROOT, data_file_name)

    print("Loading {}...".format(data_file_name))
    with open(data_path, "r") as data_fp:
        data = json.load(data_fp)

    print("Making graph...")
    graph = make_graph(data)

    personalization_file_path = os.path.join(PERSONALIZATION_ROOT, "personalization_" + data_file_name)
    print("Loading {}...".format(personalization_file_path))
    with open(personalization_file_path) as fp:
        personalization = json.load(fp)

    print("Calculating PageRank...")
    pagerank = nx.pagerank(graph, personalization=personalization)

    with open(os.path.join(PAGERANK_ROOT, "pagerank_" + data_file_name), "w+") as fp:
        json.dump(pagerank, fp)

