import math

import networkx as nx
from networkx.algorithms.dag import topological_sort
from networkx.algorithms.simple_paths import is_simple_path
from networkx.classes import subgraph


def load_file(filename):
    with open(filename) as f:
        data = f.readlines()
    data = [line.strip() for line in data]
    # Evil tuple unpacking! V
    (index_of_newline,) = [i for i, c in enumerate(data) if c == "" ]
    rules = data[:index_of_newline]
    pages = data[(index_of_newline + 1):]

    rules = [rule.split("|") for rule in rules]
    rules = [tuple(map(int, rule)) for rule in rules]

    pages = [[int(i) for i in page.split(",")] for page in pages]
    return rules, pages


def build_graph(rules):
    G = nx.DiGraph()
    G.add_edges_from(rules)
    return G

def find_valid_pages(graph, pages):
    return [page for page in pages if is_simple_path(graph, page)]

def find_invalid_pages(graph, pages):
    return [page for page in pages if not is_simple_path(graph, page)]

def add_middle(pages):
    return sum(page[math.floor(len(page)/2)] for page in pages)

def put_in_order(graph, invalid_pages):
    return [list(topological_sort(subgraph(graph, page))) for page in invalid_pages]


def main():
    rules,pages = load_file("../input")
    graph = build_graph(rules)
    valid_pages = find_valid_pages(graph, pages)
    print("Part 1:", add_middle(valid_pages))

    invalid_pages = find_invalid_pages(graph, pages)
    ordered = put_in_order(graph, invalid_pages)
    print("Part 2:", add_middle(ordered))

if __name__ == "__main__":
    main()

