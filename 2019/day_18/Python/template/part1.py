from load_input import get_input

# Target: How many steps is the shortest path that collects all of the keys?
#
# Not all keys have doors
#
# Doors open as key is picked up
#
# Keys aren't in alphabetical order


class Solver():
    # available_directions depending on walls
    # visible keys
    # seen doors

    def __init__(self, input_data):
        self.input_data = input_data
        self.current_position = None
        self._find_at()

    def look(self):
        pass

    def decide(self):
        pass

    def move(self):
        pass

    def _available_directions(self):
        pass

    def _find_at(self):
        for row_index, row in enumerate(self.input_data):
            for col_index, character in enumerate(row):
                if character == '@':
                    self.current_position = (row_index, col_index)
                    return

    def _find_visible_keys(self):
        return []


def count_steps(input_data):
    return ""


def main():
    input_data = get_input()
    return count_steps(input_data)


if __name__ == '__main__':
    print(main())
