from common import loaders


def interpret_input(input):
    caves = {}
    for line in input:
        left, right = line.split("-")

        if is_big_cave(left) and is_big_cave(right):
            ValueError("bother two big caves next to each other")

        if left not in caves.keys():
            caves[left] = set()
        if right not in caves.keys():
            caves[right] = set()
        caves[left].add(right)
        caves[right].add(left)

    return caves


def is_big_cave(cave):
    return cave.isupper()


def pathfind(caves, path):
    end_cave = "end"
    here = path[-1]

    small_caves_visited = [cave for cave in path if not is_big_cave(cave)]

    if here == end_cave:
        return 1

    possible_places_to_go = caves[here].difference(small_caves_visited)

    # try routes from this point
    out = 0
    for there in possible_places_to_go:
        out += pathfind(caves, path + [there])

    return out


def is_navigable_to(path, there):

    # options:
    # 1. there is start, we can't go back to start -> false
    # 2. We've not been there before -> true
    # 2. there is a small cave
    # 2.1 We've not been to any other small cave twice -> true
    # 2.2 We have been to a small cave twice but not this cave -> true
    # 2.3 We have been to this small cave twice already OR we have been to a different small cave twice
    # 3. there is a big cave -> true

    if there == "start":
        return False
    elif there not in path:
        return True
    elif there.islower():
        # if we've not been anywhere twice, its cool!
        if len(set(path)) == len(path):
            return True
        else:
            return False
    elif there.isupper():
        return True


def pathfind_2(caves, path):
    end_cave = "end"
    here = path[-1]

    if here == end_cave:
        print(path)
        return 1

    possible_places_to_go = [cave for cave in caves[here] if is_navigable_to(path, cave)]

    # try routes from this point
    out = 0
    for there in possible_places_to_go:
        out += pathfind_2(caves, path + [there])

    return out


if __name__ == "__main__":
    input = loaders.load_string()
    caves = interpret_input(input)
    number_of_paths = pathfind(caves, ["start"])
    number_of_paths_2 = pathfind_2(caves, ["start"])
    print(f"Part 1: {number_of_paths}")
    print(f"Part 2: {number_of_paths_2}")
