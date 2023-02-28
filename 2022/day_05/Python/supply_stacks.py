# TODO:
# 1. read in the file, split it at the blank line and then handle the crates
# 2. move the crates according to instructions
from common.loaders import load_string
import os
import __main__


def parse_crates():
    filepath = os.path.join(os.path.dirname(__main__.__file__), "../input.txt")

    with open(filepath) as file_handle:
        raw = file_handle.readlines()
    split = raw.index("\n")
    raw_crates = raw[0:split]
    raw_instructions = raw[split + 1:]

    number_stacks = int(raw_crates[split - 1][-2]) - 1
    all_stacks = {stack: [] for stack in range(1, number_stacks + 2)}
    for row in reversed(raw_crates[:-1]):
        for i, j in enumerate(range(1, len(row), 4)):
            if row[j] != " ":
                all_stacks[i + 1].append(row[j])

    return all_stacks, raw_instructions


def move(crates, quantity, start_col, end_col):
    for _ in range(quantity):
        crates[end_col].append(crates[start_col].pop())

    return crates


def move_stack(crates, quantity, start_col, end_col):
    moving_crates = crates[start_col][-quantity:]
    crates[start_col] = crates[start_col][:-quantity]
    crates[end_col].extend(moving_crates)
    return crates


def move_crates(crates, instructions):
    for instruction in instructions:
        split = instruction.strip("\n").split(" ")
        crates = move(crates, int(split[1]), int(split[3]), int(split[5]))
    return crates


def move_crates_2(crates, instructions):
    for instruction in instructions:
        split = instruction.strip("\n").split(" ")
        crates = move_stack(crates, int(split[1]), int(split[3]), int(split[5]))
    return crates

if __name__ == "__main__":
    all_stacks, instructions = parse_crates()
    #crates = move_crates(all_stacks, instructions)
    crates2 = move_crates_2(all_stacks, instructions)
    top_crates = "".join([crates2[col][-1] for col in range(1, 10)])
    print(top_crates)
