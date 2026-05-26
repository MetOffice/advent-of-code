from functools import reduce
import operator
from typing import Set, Any

import numpy as np


def read_file():
    with open("../input.txt", "r") as file:
        lines = file.readlines()
    return np.array([[int(a) for a in line.strip().split(",")] for line in lines])


def calc_distance(point1, point2):
    # 3d points
    np.linalg.norm(point1 - point2)
    return np.sqrt(np.sum((point1 - point2) ** 2))


def calc_pairs(array):
    result = []
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            result.append((calc_distance(array[i], array[j]), i, j))
    return result


def get_cluster(node, pairs, existing_clusters):
    cluster = {node}
    cluster_size = 0
    while len(cluster) != cluster_size:
        cluster_size = len(cluster)
        for _, a, b in pairs:
            if a in cluster:
                cluster.add(b)
            elif b in cluster:
                cluster.add(a)
    return cluster


def node_already_in_cluster(clusters, node):
    for cluster in clusters:
        if node in cluster:
            return True
    return False

def get_cluster_2(node: object, clusters: list[set]) -> Set | None:
    for cluster in clusters:
        if node in cluster:
            return cluster
    return None

def main():
    lines = read_file()
    pairs = calc_pairs(lines)
    pairs_sorted = sorted(pairs, key=lambda tup: tup[0])
    print(lines)
    # print(pairs_sorted)
    clusters = []
    nodes_in_clusters: Set = set()
    for pair in pairs_sorted:
        # Add to clusters
        # Neither node is in a cluster, create new cluster with both nodes
        # One node is in a cluster, add the other node to that cluster
        # Both nodes are in different clusters, merge the clusters
        a = pair[1]
        b = pair[2]
        nodes_in_clusters.add(a)
        nodes_in_clusters.add(b)

        a_cluster: Set | None = get_cluster_2(a, clusters)
        b_cluster: Set | None = get_cluster_2(b, clusters)

        if a_cluster is None and b_cluster is None:
            clusters.append({a,b})
        elif a_cluster == b_cluster:
            a_cluster.add(a)
            a_cluster.add(b)
        elif a_cluster is None and b_cluster is not None:
            b_cluster.add(a)
        elif a_cluster is not None and b_cluster is None:
            a_cluster.add(b)
        elif a_cluster != b_cluster:
            a_cluster.update(b_cluster)
            clusters.remove(b_cluster)

        # Check
        if len(nodes_in_clusters) == len(lines) and len(clusters) == 1:
            print("DONE")
            print(a)
            print(b)
            print(lines[a])
            print(lines[b])
            print("Pt2 Answer:",lines[a][0] * lines[b][0])
            break




    print("DONE")


if __name__ == "__main__":
    main()
