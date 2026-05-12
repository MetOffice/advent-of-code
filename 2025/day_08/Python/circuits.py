from functools import reduce
import operator

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


def main():
    lines = read_file()
    pairs = calc_pairs(lines)
    first_thousand = sorted(pairs, key=lambda tup: tup[0])[:1000]
    print(lines)
    print(first_thousand)
    nodes = set()
    for _, a, b in first_thousand:
        nodes.add(a)
        nodes.add(b)
    print(nodes)
    clusters = []
    for node in nodes:
        if node_already_in_cluster(clusters, node):
            continue
        clusters.append(get_cluster(node, first_thousand, clusters))
        # Part 2: can't use get_cluster, have to do incremental cluster
        # update for each pair
    clusters.sort(key=len, reverse=True)
    print("All circuits ", clusters)
    print(clusters[:3])
    print(reduce(operator.mul, map(len, clusters[:3]), 1))


if __name__ == "__main__":
    main()
