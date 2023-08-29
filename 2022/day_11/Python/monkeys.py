
from typing import List, Tuple

class Monkey:
    """
    A monkey carries a list of items and can inspect and throw them
    """

    def __init__(self,
                 items:List[int],
                 test_divisor:int,
                 inspect_function:function,
                 true_target:int,
                 false_target:int
    ) -> None:
        # The only property an item has is its worry level
        self.items = items
        # The factor used to determine target
        self.test_divisor = test_divisor
        # The function used to adjust worry on inspection
        self.inspect_function = inspect_function
        # Target for if test is true
        self.true_target = true_target
        # Target for if test is false
        self.false_target = false_target
        # Count how many items I have inspected
        self.inspections = 0

    
    @staticmethod
    def construct_from_string(input_string:str) -> "Monkey":
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
        operation_string = operation_line.split("old")[1]
        op, arg = operation_string.split()
        inspect_function = Monkey.create_inspect_function(op, arg)


    @staticmethod
    def create_inspect_function(op:str, arg:str) -> function:
        """
        Create the operation for altering worry level
        """
        if arg == "old":
            return lambda x: Monkey.times_or_plus(op)(x, x)
        else:
            param = int(arg)
            return lambda x: Monkey.times_or_plus(op)(x, param)

    @staticmethod
    def times_or_plus(op:str) -> function:
        if op == "*":
            return lambda x, y: x * y
        if op == "+":
            return lambda x, y: x + y
        raise Exception(f"{op} is not an operator")

    def inspect_all(self):
        """
        Inspect all my items
        """
        self.items = [self.inspect_function(item) for item in self.items]
        self.inspections += len(self.items)

    def throw_all(self) -> List[Tuple[int,int]]:
        """
        Declare all throws I intend to make
        """
        passes = [self.throw(item) for item in self.items]
        self.items = []
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
        self.items.append(item)


class Barrel:
    """
    A collection of monkeys is called a barrel.
    It deals with throwing and comparisons between monkeys.
    """
    def __init__(self, monkeys:List[Monkey]) -> None:
        self.monkeys = monkeys

    @staticmethod
    def construct_from_string(input_string:str) -> "Barrel":
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