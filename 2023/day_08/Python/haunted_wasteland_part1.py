import multiprocessing as mp

test_data = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""

#! Ignore me
'''class Node:
    entrance: str
    exits: tuple[Self, Self]'''

def load_data(filename: str) -> tuple[str, list[str]]:
    """Loads the initial datafile

    Args:
        filename (str): The name of the file

    Returns:
        str, list[str]: The instructions and the formatted nodes
    """

    with open(filename, "r") as file:
        data = file.readlines()

    # First line is instructions
    instructions = data[0].strip()

    # Format the nodes
    nodes = data[2:]

    nodes = separate_nodes(nodes)

    return instructions, nodes


def separate_node(node: str) -> tuple[str, str]:
    """Splits nodes into entrance and exits

    Args:
        node (str): The unformatted node loaded from the file

    Returns:
        tuple[str, str]: The two possible exits for this node.
    """

    entrance, exits = node.strip().split(" = ")

    # Format exits
    exits = tuple(exits.replace("(", "").replace(")", "").split(", "))

    return entrance, exits


def separate_nodes(nodes: list[str]) -> list[tuple[str, str]]:
    """Splits all nodes into entrance and exits

    Args:
        nodes (list[str]): The unformatted nodes loaded from the file

    Returns:
        list[tuple[str, str]]: The formatted nodes
    """

    formatted_nodes = []

    for node in nodes:
        entrance, exits = separate_node(node)
        formatted_nodes.append((entrance, exits))

    return formatted_nodes


def nodes_to_dict(nodes):
    nodes_dict = {}

    for node in nodes:
        nodes_dict[node[0]] = {
            "L": node[1][0],
            "R": node[1][1]
        }

    return nodes_dict

if __name__ == "__main__":
    instructions, nodes = load_data("./data.txt")

    # Convert the nodes to a dictionary
    nodes_dict = nodes_to_dict(nodes)

    node_count = 0
    traversed_nodes = []

    current_node = "AAA"

    while current_node != "ZZZ":
        current_node = nodes_dict[current_node][instructions[node_count]]
        traversed_nodes.append(current_node)
        node_count += 1
        if node_count > len(instructions) - 1:
            node_count = 0

    print(len(traversed_nodes))
