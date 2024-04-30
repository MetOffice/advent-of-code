from dataclasses import dataclass

from loaders import load_string


@dataclass
class MapRange:
    destination_start: int
    source_start: int
    range_length: int

    def destination_index(self, source_index: int) -> int | None:
        if self.source_start <= source_index < self.source_start + self.range_length:
            return source_index - self.source_start + self.destination_start

        return None

@dataclass
class Map:
    source_name: str
    destination_name: str

    ranges: list[MapRange]

    def apply(self, source_index: int) -> int:
        for map_range in self.ranges:
            destination_index = map_range.destination_index(source_index)
            if destination_index:
                return destination_index

        return source_index

    def apply_to_list(self, source_indices: list[int]) -> list[int]:
        return list(map(self.apply, source_indices))


    @staticmethod
    def from_input(input_str: str) -> 'Map':

        # the first line will make the name
        first_line, *other_lines = input_str.split("\n")
        source_name, destination_name = first_line.split(" ")[0].split("-to-")
        ranges = []
        for line in other_lines:
            destination_start, source_start,  range_length = line.split(" ")
            ranges.append(MapRange(int(destination_start), int(source_start), int(range_length)))

        # the rest is all the MapRanges
        return Map(source_name, destination_name, ranges)


def parse_input(input_string: str) -> tuple[list[int], list[Map]]:

    first_line, *everything_else = input_string.split('\n\n')

    # handle first line to get the seeds
    seeds = list(map(int, first_line.split(':')[1].split()))

    # unpack the everything_else
    the_maps = []
    for thing in everything_else:
        # make a Map
        the_maps.append(Map.from_input(thing))


    return seeds, the_maps


def get_lowest_location(seeds, maps):
    map_dict = {index_map.source_name: index_map for index_map in maps}

    things = seeds
    current_thing = "seed"

    while current_thing != "location":
        current_map = map_dict[current_thing]
        things = current_map.apply_to_list(things)
        current_thing = current_map.destination_name

    return min(things)


if __name__ == "__main__":
    input_data = "../input.txt"
    with open(input_data) as file:
        input_string = file.read()

    seeds, maps = parse_input(input_string)
    lowest = get_lowest_location(seeds, maps)
    print(lowest)