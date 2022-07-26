from dataclasses import dataclass

@dataclass
class FishTimes:
    reproduction_cycle:int
    growth:int

    def max(self):
        """
        The max state any fish can have
        """
        return self.reproduction_cycle + self.growth


def setup_pop(input:str, timings:FishTimes):
    """
    Reads input and creates the initial population
    Pop is a 9 element list, where the element at index n is the number of fish
    with internal count n
    """
    raw_pop = [int(fish) for fish in input.split(",")]
    pop = [0] * timings.max()
    for fish in raw_pop:
        pop[fish] += 1
    return pop


def total_lanternfish(pop, timings:FishTimes, generations:int):
    """
    Simulates the reproduction of the pop for the given number of generations
    """
    for _ in range(generations):
        # Remove all time 0 fish and record their number
        babs = pop.pop(0)
        # Add children for those fish
        pop.append(babs)
        # Those fish continue in state 6
        pop[timings.reproduction_cycle - 1] += babs

    return sum(pop)


def main():
    with open("./2021/day_06/input.txt", "r") as file:
        input = file.read()

    times = FishTimes(7, 2)
    generations = 256

    pop = setup_pop(input, times)
    total = total_lanternfish(pop, times, generations)
    print(total)

if __name__ == "__main__":
    main()