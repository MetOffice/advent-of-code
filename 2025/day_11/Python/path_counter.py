from functools import cache

def load_input(file_path) -> dict[str, list[str]]:
    with open(file_path, "r") as f:
        lines = f.read().splitlines()

    # Don't judge me
    stuff = {}
    for line in lines:
        key, value = line.split(":")
        value = value.split(" ")
        value = value[1:]
        stuff[key] = value

    return stuff


def is_out(string):
    if string == "out":
        return True
    else:
        return False

@cache
def count_paths(device):
    num_paths = 0
    for sub_device in PATHS[device]:
        if is_out(sub_device):
            num_paths += 1
        else:
            num_paths += count_paths(sub_device)
    return num_paths

@cache
def iterate_paths(device: str) -> list[list[str]]:
    seen_thing: list[list[str]] = []
    for sub_device in PATHS[device]:
        if is_out(sub_device):
            seen_thing.append(["out"])
        else:
            seen_thing.extend([sub_device, *path] for path in iterate_paths(sub_device))
    return seen_thing

if __name__ == "__main__":
    PATHS = load_input("input.txt")
    start = "you"

    partA = count_paths(start)
    print("Part A:", partA)

    # DON'T RUN THIS IT WILL BREAK THINGS
    #partB_paths = iterate_paths("svr")
    #okay_paths = [path for path in partB_paths if "dac" in path and "fft" in path]
    #print("Part B:", len(okay_paths))