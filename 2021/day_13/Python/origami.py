from typing import List, Tuple
from common import loaders


def interpret_input(instructions):
    split_location = instructions.index("")
    coordinates = instructions[0:split_location]
    folding_instructions = instructions[split_location + 1 :]
    return coordinates, folding_instructions


def split_folding_instructions(
    folding_instructions: List[str],
) -> List[Tuple[str, int]]:

    new_folding_instructions = []
    for folding_instruction in folding_instructions:
        axis = folding_instruction[11]
        line = int(folding_instruction[13:])
        new_folding_instruction = (axis, line)
        new_folding_instructions.append(new_folding_instruction)

    return new_folding_instructions


def split_coordinates(coordinates):
    x_list = [int(item.split(",")[0]) for item in coordinates]
    y_list = [int(item.split(",")[1]) for item in coordinates]
    return x_list, y_list


class Paper:
    def __init__(self, x_list, y_list):
        self.x_list = x_list
        self.y_list = y_list

    def apply_single_fold(self, folding_instruction: Tuple[str, int]):
        if folding_instruction[0] == "x":
            self.x_list = [
                self.find_new_coordinate_value(folding_instruction, position)
                for position in self.x_list
            ]

        else:
            self.y_list = [
                self.find_new_coordinate_value(folding_instruction, position)
                for position in self.y_list
            ]

    def apply_folds(self, folding_instructions):
        for instr in folding_instructions:
            self.apply_single_fold(instr)

    def find_new_coordinate_value(self, folding_instruction, position):
        return folding_instruction[1] - abs(position - folding_instruction[1])

    def count_dots(self):
        result = set(zip(self.x_list, self.y_list))
        return len(result)

    def __str__(self):
        max_x = max(self.x_list)
        max_y = max(self.y_list)
        row = [" "] * (max_x + 1)
        canvas = [row.copy() for i in range(max_y + 1)]
        for x, y in set(zip(self.x_list, self.y_list)):
            canvas[y][x] = "#"
        return "\n".join(["".join(row) for row in canvas])


def part1():
    instructions = loaders.load_string()
    coordinates, folding_instructions = interpret_input(instructions)
    x_list, y_list = split_coordinates(coordinates)
    folding_instructions = split_folding_instructions(folding_instructions)
    paper = Paper(x_list, y_list)
    paper.apply_single_fold(folding_instructions[0])
    answer_1 = paper.count_dots()
    return answer_1


def part2():
    instructions = loaders.load_string()
    coordinates, folding_instructions = interpret_input(instructions)
    x_list, y_list = split_coordinates(coordinates)
    folding_instructions = split_folding_instructions(folding_instructions)
    paper = Paper(x_list, y_list)
    paper.apply_folds(folding_instructions)
    print(paper)
    return


if __name__ == "__main__":
    print(f"Part 1 answer: {part1()}")
    print("Day 2 answer:")
    part2()
