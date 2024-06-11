from dataclasses import dataclass
from typing import Optional

from loaders import load_string

@dataclass
class ItemRange:
    source_start: int
    range_length: int

    @property
    def source_end(self):
        return self.source_start + self.range_length
    
    def contains(self, idx:int):
        """
        Does this range contain the given index?
        """
        return self.source_start <= idx < self.source_end


@dataclass
class MapRange:
    destination_start: int
    source_start: int
    range_length: int

    def destination_index(self, source_index: int) -> int | None:
        if self.source_start <= source_index < self.source_end:
            return source_index + self.mapping_offset

        return None
    
    @property
    def source_end(self):
        return self.source_start + self.range_length
    
    @property
    def mapping_offset(self):
        return self.destination_start - self.source_start
    
    def intersects_with(self, item_range:ItemRange) -> bool:
        """
        Does the given item range intersect with the source range?
        """
        # One or both of these should be a <= D:
        return self.source_end > item_range.source_start and self.source_start < item_range.source_end
    
    def intersection(self, item_range:ItemRange) -> tuple[ItemRange, ItemRange]:
        """
        Get the intersection of overlapping item_range in source and destination index.
        """
        lower_bound = max(self.source_start, item_range.source_start)
        upper_bound = min(self.source_end, item_range.source_end)
        range_length = upper_bound - lower_bound

        source_range = ItemRange(lower_bound, range_length)
        destination_range = ItemRange(lower_bound + self.mapping_offset, range_length)

        return source_range, destination_range


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
    def from_input(input_str: str) -> "Map":

        # the first line will make the name
        first_line, *other_lines = input_str.split("\n")
        source_name, destination_name = first_line.split(" ")[0].split("-to-")
        ranges = []
        for line in other_lines:
            destination_start, source_start, range_length = line.split(" ")
            ranges.append(
                MapRange(int(destination_start), int(source_start), int(range_length))
            )

        # the rest is all the MapRanges
        return Map(source_name, destination_name, ranges)


def parse_input(input_string: str) -> tuple[list[int], list[Map]]:

    first_line, *everything_else = input_string.split("\n\n")

    # handle first line to get the seeds
    seeds = list(map(int, first_line.split(":")[1].split()))

    # unpack the everything_else
    the_maps = []
    for thing in everything_else:
        # make a Map
        the_maps.append(Map.from_input(thing))

    return seeds, the_maps


# Part 1
def get_lowest_location(seeds, maps):
    map_dict = {index_map.source_name: index_map for index_map in maps}

    things = seeds
    current_thing = "seed"

    while current_thing != "location":
        current_map = map_dict[current_thing]
        things = current_map.apply_to_list(things)
        current_thing = current_map.destination_name

    return min(things)


# Part 2
def get_lowest_seed(
    seed_ranges: list[tuple[int, int]],
    maps: list[Map],
    within_limits: Optional[tuple[int, int]] = None,
):
    if not maps:
        assert within_limits
        for seed_range in seed_ranges:
            top = seed_range[0] + seed_range[1]
            bottom = seed_range[0]
            if bottom >= within_limits[1]:
                continue
            if top < within_limits[0]:
                continue

            if within_limits[0] <= seed_range[0]:
                return seed_range[0]
            else:
                return within_limits[0]

        return None

    else:
        current_range_start = within_limits[0] if within_limits else 0

        # First range that goes past the start
        source_ranges = iter(sorted(maps[-1].ranges, key=lambda r: r.source_start))
        next_source_range = next(source_ranges)
        while next_source_range.source_start + next_source_range.range_length <= current_range_start:
            next_source_range = next(source_ranges)
        destination_ranges = iter(
            sorted(maps[-1].ranges, key=lambda r: r.destination_start)
        )
        next_dest_range = next(destination_ranges)
        while next_dest_range.destination_start + next_dest_range.range_length <= current_range_start:
            next_dest_range = next(destination_ranges)

        # Current if it includes the start
        current_source_range = (
            next_source_range
            if next_source_range.source_start <= current_range_start
            and (
                next_source_range.source_start + next_source_range.range_length
                > current_range_start
            )
            else None
        )
        if current_source_range:
            next_source_range = next(source_ranges)
        current_dest_range = (
            next_dest_range
            if next_dest_range.destination_start <= current_range_start
            and (
                next_dest_range.destination_start + next_dest_range.range_length
                > current_range_start
            )
            else None
        )
        if current_dest_range:
            next_dest_range = next(destination_ranges)

        while within_limits is None or current_range_start < within_limits[1]:
            if current_dest_range:
                result = get_lowest_seed(seed_ranges, maps[:-1], (current_range_start, current_dest_range.destination_start + current_dest_range.range_length))
                pass

    # trying depth first search first before the paragraph below
    # - choose lowest range (including not-MapRanges) within limits
    # - compute what sub ranges the next map will split those into,
    #   doing the map backwards
    # - recurse depth first starting with the lowest range, and
    #   then increasing if a seed is not found

    # 28/05/2024
    # Multiple ranges could go to the same place, including unmapped ranges
    # You know what, maybe do it ↓ that way ↓ after all

    # seeds is a collection of ranges now...
    # (seednum, range), (seednum, range) -> (start1, end1), (start2, end2)
    # we will need to apply a MapRange to a range of source numbers, to create destination ranges
    # we will do this for all the MapRanges in a Map... account for possible overlaps in a Map
    # repeat for all Maps
    # find the lowest bound of any of them
    # voila
    raise NotImplementedError


if __name__ == "__main__":
    input_data = "../input.txt"
    with open(input_data) as file:
        input_string = file.read()

    seeds, maps = parse_input(input_string)
    lowest = get_lowest_location(seeds, maps)
    print(lowest)

    seed_ranges = [ItemRange(*item) for item in zip(seeds[::2], seeds[1::2])]

    pass


# Brute Force Method
    
# Make numpy arrays where each entry is the value that index goes to
#   - So if 3 -> 4 then we can have [0,1,2,4,4,5,...]
# to build
    # Start with range [0,...,999999]
    # for each map add the displacement to the index on a slice
# Do massive index chain like reachable_locations = location[...[fertiliser[soils[seeds]]]...]
# min(that)
    


def get_lowest_seed(seed_ranges: list[ItemRange], maps: list[Map]) -> int:
    """
    TODO: Make this docstring vaguely representative of what we end up with.
    Ranges moving method
    We consider the ranges and their start/end points.
    We find their image post mapping.
    Repeat for each mapping.
    Find the lowest endpoint at the end.

    Start with seed ranges
    Delete any portion that is mapped
    Include mapped versions of those deleted portions
    """

    # A ranges first approach
    # For each range in turn
    #- Find any maps that cross into it
    #- Create all child ranges
    pass
    

def apply_map_to_ranges(item_ranges:list[ItemRange], mapping:Map):
    map_ranges = mapping.ranges

    for item_range in item_ranges:
        poststep_ranges = []
        snips = []

        for map_range in map_ranges:
            if not map_range.intersects_with(item_range):
                continue
            
            # Want a pre step collection and post step collection


            # I would like
            # - to get the image by the map range
            source_snip, destination_image = map_range.intersection(item_range)

            poststep_ranges.append(destination_image)
            snips.append(source_snip)


            # - to snip out all the preimages from the item range
            # - - Then at end add remainder to post step collection to the post step to allow passthroughs
            

