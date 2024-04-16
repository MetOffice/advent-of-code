from dataclasses import dataclass

from loaders import load_string


@dataclass
class MapRange:
    source_start: int
    destination_start: int
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


def parse_input(input_str: list[str]) -> tuple[list[int], list[Map]]:
    input_iter = iter(input_str)

    seeds = list(map(int, next(input_iter).split(':')[1].split()))

    try:
        while True:
            line = next(input_iter)
    except StopIteration:
        pass

def get_lowest_location():
    seeds, maps = parse_input(load_string())

    map_dict = {index_map.source_name: index_map for index_map in maps}

    things = seeds
    current_thing = "seed"

    while current_thing != "location":
        current_map = map_dict[current_thing]
        things = current_map.apply_to_list(things)
        current_thing = current_map.destination_name

    return min(things)
