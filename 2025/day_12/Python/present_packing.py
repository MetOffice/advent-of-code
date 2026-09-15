from dataclasses import dataclass, field
from functools import cache
from typing import Literal, Self
import numpy as np


type D4 = Literal["1", "2", "3", "4", "1F", "2F", "3F", "4F"]


@dataclass
class Present:
    idx: int
    shape: np.ndarray
    shapes: dict[D4, np.ndarray]

    @classmethod
    def parse_present(cls, p) -> Self:
        idx, shape = p.split(":")
        shape_split = shape.strip().split("\n")
        shape = np.array([[i == "#" for i in o] for o in shape_split])

        shapes = {}
        for rotation in [0, 1, 2, 3]:
            rotated_shape = np.rot90(shape, rotation)
            for flip, new_shape in [
                ("", rotated_shape),
                ("F", np.flip(rotated_shape)),
            ]:
                if not any(np.array_equal(new_shape, a) for a in shapes):
                    shapes[f"{rotation}{flip}"] = new_shape

        ##Symmetries as well
        return cls(int(idx), shape, shapes)


def parse_present_shapes(present_shapes: list[str]) -> list[Present]:
    return [Present.parse_present(shape) for shape in present_shapes]


@dataclass
class Tree:
    width: int
    height: int
    present_quantities: list[int]

    @classmethod
    def parse_tree(cls, t: str) -> Self:
        shape, present = t.strip().split(":")
        width, height = shape.split("x")
        presents = [int(i) for i in present.strip().split(" ")]

        return cls(int(width), int(height), presents)


@dataclass(frozen=True)
class PlacedPresent:
    shape_index: int
    top: int
    left: int
    flippiness: D4


@dataclass(frozen=True)
class PopulatedGrid:
    presents: tuple[PlacedPresent, ...]
    grid: np.ndarray = field(hash=False)


@cache
def can_populate(
    width: int,
    height: int,
    grid: PopulatedGrid,
    remaining_presents: tuple[int, ...],
    present_shapes: tuple[Present, ...],
) -> bool:
    try:
        shape_index, _ = next(
            (i, n) for i, n in enumerate(remaining_presents) if n > 0
        )
    except StopIteration:
        return True

    for d4, shape in present_shapes[shape_index].shapes.items():
        for i in range(width - shape.shape[0] + 1):
            for j in range(height - shape.shape[1] + 1):
                grid_copy = grid.grid.copy()
                cutout = grid_copy[
                    i : i + shape.shape[0], j : j + shape.shape[1]
                ]
                cutout &= shape
                if not np.any(cutout):
                    cutout |= shape
                    next_remaining_presents = tuple(
                        n - 1 if i == shape_index else n
                        for i, n in enumerate(remaining_presents)
                    )
                    if can_populate(
                        width,
                        height,
                        PopulatedGrid(
                            presents=(
                                *grid.presents,
                                PlacedPresent(shape_index, i, j, d4),
                            ),
                            grid=grid_copy,
                        ),
                        next_remaining_presents,
                        present_shapes,
                    ):
                        return True

    return False


def parse_trees(trees: list[str]):
    return [Tree.parse_tree(t) for t in trees]


def load_file(file):
    with open(file) as f:
        contents = f.read()
        *present_shapes, trees = contents.split("\n\n")
        return parse_present_shapes(present_shapes), parse_trees(
            trees.split("\n")
        )
        print(contents)


def main():
    a, b = load_file("input.txt")
    # Need to use can_populate on all regions and count up ok bye
    print(a, b)


if __name__ == "__main__":
    main()
