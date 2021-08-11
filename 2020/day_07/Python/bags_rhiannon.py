from typing import Dict, List
from common import loaders, timers
import numpy as np


def flatten(l: List) -> List:
    """

    Parameters
    ----------
    l : list
         List with more lists inside

    Returns
    -------
    list
        A flattened list
    """
    if l:
        if isinstance(l[0], list):
            return [item for sublist in l for item in sublist]
        else:
            return l
    else:
        return l


def parse_bag_rule(bag_rule: str) -> List[str]:
    """
    Formats a bag rule string into a more useful list

    Parameters
    ----------
    bag_rule : str
        A string for example "light red bags contain 1 bright white bag, 2 muted yellow bags."

    Returns
    -------
    list :
        formatted string as list e.g. ["light red", "1 bright white", "2 muted yellow"],

    """

    results = []
    contains_str = "bags contain"
    cleaned = [item.strip() for item in bag_rule.split(contains_str)]

    # We've finished with the 1st element - remove it!
    results.append(cleaned.pop(0))

    multi_str = ", "
    contained = cleaned[0].split(multi_str)
    contained = [
        item.replace("bags", "").replace("bag", "").replace(".", "").strip()
        for item in contained
    ]

    results.extend(contained)

    return results


def parse_bag_rules(bag_rules: List[str]) -> Dict:
    """

    Parameters
    ----------
    bag_rules :
        A list of strings containing bag rules

    Returns
    -------
    dict
        A dictionary containing the organised rules
        e.g. {outer_bag: [{child1: count1}, {child2: count2}, ....]

    """

    organised_rules = {}
    for line in bag_rules:
        parsed = parse_bag_rule(line)
        key = parsed.pop(0)
        inner_list = []
        organised_rules[key] = inner_list
        for item in parsed:
            number, bag_colour = item.split(maxsplit=1)
            if number != "no":
                inner_list.append({bag_colour: int(number)})

    return organised_rules


def find_all_paths_from_one_node(graph, start, end=None, path=[]) -> List:
    """
    Finds all the paths in the graph from the named node start. Using a depth first search.
    If end is supplied then all paths will end at that node, else when they reach the bottom of the tree.

    Parameters
    ----------
    graph : dict
        A dictionary containing lists of dictionaries, representing {parent_node1: [{child1: count1}, {child2: count2},...], }
    start : str
        The name of the first node we will start searching from
    end :
        The final node, optional
    path :
        Optional

    Returns
    -------
    list :
        A list of lists containing all the routes from start to end (or bottom)

    """

    path = path + [start]

    if start not in graph.keys():
        return []
    if end is None:
        if not graph[start]:
            # i.e. if it is empty
            return [path]
    if end is not None:
        if start == end:
            return[path]

    paths = []
    for node in graph[start]:
        node_name = list(node.keys())[0]
        if node_name not in path:
            newpaths = find_all_paths_from_one_node(graph, node_name, end=end, path=path)
            for newpath in newpaths:
                if end is not None:
                    if end in newpath:
                        paths.append(newpath)
                else:
                    paths.append(newpath)

    return paths


def get_all_paths_to_node_from_graph(graph, end_node):
    """
    For all the possible start nodes, find the paths to end node

    Parameters
    ----------
    graph : dict
        the graph file
    end_node : str
        The end node we want to find paths to

    Returns
    -------
    list :
        A list of lists of all possible paths

    """
    all_paths = []
    flat_all_paths = []
    for node in graph.keys():
        if node not in flat_all_paths:
            # print(f"working on {node}")
            paths_from_this_node = find_all_paths_from_one_node(graph, node, end=end_node)
            if paths_from_this_node:
                all_paths.append(paths_from_this_node)
                flat_all_paths.append(flatten(paths_from_this_node))

    return all_paths


@timers.print_duration
def find_count_possible_outermost_bags(bag_rules : List[str], child_bag: str) -> int:
    """
    Gets the count of all the possible outermost bags which could contain child bag eventually be inside.

    Parameters
    ----------
    bag_rules : list[str]
        List or strings of bag rules
    child_bag : str
        The name of the child bag of interest

    Returns
    -------
    int
        The count of possible parent bags

    """
    organised_rules = parse_bag_rules(bag_rules)
    all_paths = get_all_paths_to_node_from_graph(organised_rules, child_bag)
    outermost_bags = []
    for path_set in all_paths:
        bag = path_set[0][0]
        if bag != child_bag:
            outermost_bags.append(bag)

    final_outermost = list(set(outermost_bags))

    return len(final_outermost)


def get_max_num_of_bags_inside(bag_rules: List[str], bag_name: str) -> int:
    """
    Gets the count of how many bags could be inside a bag_name bag

    Parameters
    ----------
    bag_rules : list[str]
        List or strings of bag rules
    bag_name : str
        The name of the parent bag of interest

    Returns
    -------
    int
        The count of possible children bags
    """
    organised_rules = parse_bag_rules(bag_rules)
    all_paths_from_bag = find_all_paths_from_one_node(organised_rules, bag_name)

    # now we have all the paths from bag_name,
    # we need to traverse the graph following these paths to get the number of child bags
    count = []
    for path in all_paths_from_bag:
        path_bag_count = []
        for bag in range(1, len(path)):
            inner_bag = [elem for elem in organised_rules[path[bag-1]] if path[bag] in elem]
            path_bag_count.append(inner_bag[0][path[bag]])

        path_sum = 0
        for i in range(1, len(path_bag_count)):
            path_sum += path_bag_count[i-1] + path_bag_count[i-1] * path_bag_count[i]

        count.append(path_sum)

    return np.sum(count)


if __name__ == "__main__":
    rules = loaders.load_string()
    # count = find_count_possible_outermost_bags(rules, "shiny gold")
    #
    # print(count)
    # 372
    # part 2 = how many bags can a given bag contain?
    count2 = get_max_num_of_bags_inside(rules, "shiny gold")
    print(count2)