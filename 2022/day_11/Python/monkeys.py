import math
from cProfile import Profile
from pstats import SortKey, Stats
import re
from typing import List, Tuple, Callable, Any
import numpy as np


class Monkey:
    """
    A monkey carries a list of items and can inspect and throw them
    """

    def __init__(self,
                 items: List[int],
                 test_divisor: int,
                 true_target: int,
                 false_target: int,
                 op, right
                 ) -> None:
        # The only property an item has is its worry level
        self.items = np.asarray(items, dtype=np.int64)
        # The factor used to determine target
        self.test_divisor = test_divisor
        # The function used to adjust worry on inspection
        # self.inspect_function = inspect_function
        # Target for if test is true
        self.true_target = true_target
        # Target for if test is false
        self.false_target = false_target
        # Count how many items I have inspected
        self.inspections = 0
        self.op = op
        self.right = right

    def __str__(self):
        return f"Monkey\n" \
               f"Items: {self.items}\n" \
               f"Test: Divide by {self.test_divisor}\n" \
               f"True Target: {self.true_target}\n" \
               f"False Target: {self.false_target}\n" \
               f"Inspections: {self.inspections}\n"

    @staticmethod
    def construct_from_string(input_string: str) -> "Monkey":
        """
        Create a monkey from an input string
        """
        input_string = input_string.strip()
        input_lines = input_string.split("\n")

        items_line, operation_line, test_line, true_line, false_line = input_lines[1:6]

        # items line
        items_string = items_line.split(":")[1]
        items = items_string.split(",")
        items = [int(item) for item in items]

        # operation line
        regex = re.compile(".* new = .* (.) (.*)")
        op, right = regex.findall(operation_line)[0]
        # inspect_function = Monkey.create_inspect_function(op, right)
        test_divisor = int(test_line.split("divisible by ")[1])
        true_target = int(true_line.split("throw to monkey ")[1])
        false_target = int(false_line.split("throw to monkey ")[1])

        return Monkey(items, test_divisor, true_target, false_target, op, right)

    @staticmethod
    # def create_inspect_function(op: str, arg: str) -> Callable[[int], int]:
    #     """
    #     Create the operation for altering worry level
    #     """
    #     if arg == "old":
    #         if op == "*":
    #             return Monkey._self_times_self()
    #     else:
    #         param = int(arg)
    #         return lambda x: Monkey.times_or_plus(op)(x, param)

    # @staticmethod
    # def times_or_plus(op: str) -> Callable[[int, int], int]:
    #     if op == "*":
    #         return lambda x, y: x * y
    #     if op == "+":
    #         return lambda x, y: x + y
    #     raise Exception(f"{op} is not an operator")
    @staticmethod
    def _self_times_self(x):
        return x * x
    @staticmethod
    def _self_times_other(x, y):
        return x * y
    @staticmethod
    def _self_plus_self(x):
        return x + x
    @staticmethod
    def _self_plus_other(x, y):
        return x + y

    def inspect_all(self):
        """
        Inspect all my items
        """

        if self.op == "*":
            if self.right == "old":
                self.items = self._self_times_self(self.items)
            else:
                self.items = self._self_times_other(self.items, int(self.right))

        else:
            if self.right == "old":
                self.items = self._self_plus_self(self.items)
            else:
                self.items = self._self_plus_other(self.items, int(self.right))

        # self.items = [self.inspect_function(item) for item in self.items]
        # # self.items = [math.floor(item / 3.0) for item in self.items]
        # self.items = np.floor(self.items/3.0)
        self.inspections += len(self.items)

    def throw_all(self) -> List[Tuple[int, int]]:
        """
        Declare all throws I intend to make
        """
        passes = [self.throw(item) for item in self.items]
        self.items = np.asarray([], dtype=np.int64)
        return passes

    def throw(self, item):
        """
        Declare a throw for one of my items. I do not remove the item from my inventory because
        I do that in throw_all.
        """
        if item % self.test_divisor == 0:
            target = self.true_target
        else:
            target = self.false_target
        return target, item

    def catch(self, item):
        """
        Receive an item into my inventory
        """
        self.items = np.append(self.items, item)



class Barrel:
    """
    A collection of monkeys is called a barrel.
    It deals with throwing and comparisons between monkeys.
    """

    def __init__(self, monkeys: List[Monkey]) -> None:
        self.monkeys = monkeys

    @staticmethod
    def construct_from_string(input_string: str) -> "Barrel":
        """
        Create a new barrel using an input string
        """
        monkey_inputs = input_string.split("\n\n")
        monkeys = [Monkey.construct_from_string(monkey_input) for monkey_input in monkey_inputs]
        return Barrel(monkeys)

    def round(self):
        """
        Do all passes for one round
        """
        for monkey in self.monkeys:
            monkey.inspect_all()
            passes = monkey.throw_all()

            for target, item in passes:
                self.monkeys[target].catch(item)

    def n_rounds(self, n):
        """
        Do n rounds
        """
        for _ in range(n):
            self.round()

    def monkey_business(self):
        """
        Compute the amount of monkey business
        """
        activity = [monkey.inspections for monkey in self.monkeys]
        one, two = sorted(activity)[-2:]
        return one * two

    def __repr__(self):
        for monkey in self.monkeys:
            print(monkey)
        # TODO: fix
        return "a"

def main():
    with open("../test_input.txt", "r") as file:
        input_file = file.read()
    barrel = Barrel.construct_from_string(input_file)
    barrel.n_rounds(20)
    print(barrel)
    print(barrel.monkey_business())


if __name__ == "__main__":
    # TODO: weirdly have numerical drift after a large number of iterations?
    main()
