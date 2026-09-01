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
def count_paths2(device, seen_dac, seen_fft):
    seen_dac |= device == "dac"
    seen_fft |= device == "fft"
    num_paths = 0
    for sub_device in PATHS[device]:
        if is_out(sub_device):
            if seen_dac and seen_fft :
                num_paths += 1
        else:
            num_paths += count_paths2(sub_device, seen_dac, seen_fft)
    return num_paths

if __name__ == "__main__":
    PATHS = load_input("input.txt")
    partA = count_paths("you")
    print("Part A", partA)
    partB = count_paths2("svr", False, False)
    print("Part B", partB)
