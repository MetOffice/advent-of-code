from dataclasses import dataclass
import multiprocessing as mp
import os
from datetime import datetime

test_data = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""

#! Ignore me
"""class Node:
    entrance: str
    exits: tuple[Self, Self]"""


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
        nodes_dict[node[0]] = {"L": node[1][0], "R": node[1][1]}

    return nodes_dict


@dataclass(frozen=True)
class LocationOfZ:
    instruction_index: int
    node: str
    step_count: int


if __name__ == "__main__":

    instructions, nodes = load_data("./data.txt")

    # Convert the nodes to a dictionary
    nodes_dict = nodes_to_dict(nodes)

    instruction_index = 0
    full_count = 0

    current_nodes = [node for node in nodes_dict if node[-1] == "A"]

    #loop_detection: tuple[list[LocationOfZ], ...] = tuple([] for node in current_nodes)

    start_time = datetime.now()
    with open("output2.csv", "a") as f:
        # While any ghost is at a node not ending in Z
        while any(current_node[-1] != "Z" for current_node in current_nodes):

            # Step each ghost forward according to the current instruction direction
            current_nodes = [
                nodes_dict[current_node][instructions[instruction_index]]
                for current_node in current_nodes
            ]

            cases = [current_node[-1] == "Z" for current_node in current_nodes]
            if any(cases):
                for i, case in enumerate(cases):
                    if case:
                        print(f"{i}, {current_nodes[i]}, {instruction_index}, {full_count}", file=f)

            instruction_index += 1
            full_count += 1
            if instruction_index > len(instructions) - 1:
                instruction_index = 0
            if full_count >= 1000:
                break

        print(full_count)
    end_time = datetime.now()
    print(end_time - start_time)
    # This would have taken 3700 years to complete.
    # Instead, we wrote out any time the ghost reached a Z node.
    # Putting this in excel, each ghost looped on a regular interval.
    # The lowest common multiple of these loops is the answer
    # math.lcm(15871,21251,16409,11567,18023,14257)

