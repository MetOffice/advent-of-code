from dataclasses import dataclass
import numpy as np


@dataclass
class Present:
    idx: int
    shape: np.ndarray
    shapes: list[np.ndarray]

    @classmethod
    def parse_present(cls, p):
        idx, shape = p.split(":")
        shape_split = shape.strip().split("\n")
        shape = np.array([[i == "#" for i in o] for o in shape_split])

        shapes = []
        for rotation in [0, 1, 2, 3]:
            rotated_shape = np.rot90(shape, rotation)
            for new_shape in [
                rotated_shape,
                np.flip(rotated_shape),
                np.flip(rotated_shape, 0),
                np.flip(rotated_shape, 1)
            ]:
                if not any(np.array_equal(new_shape, a) for a in shapes):
                    shapes.append(new_shape)

        ##Symmetries as well
        return Present(int(idx), shape, shapes)


def parse_present_shapes(present_shapes: list[str]):
    return [Present.parse_present(shape) for shape in present_shapes]


@dataclass
class Tree:
    width: int
    height: int
    present_quantities: list[int]

    @classmethod
    def parse_tree(cls, t: str) -> Tree:
        shape, present = t.strip().split(":")
        width, height = shape.split("x")
        presents = [int(i) for i in present.strip().split(" ")]

        return cls(int(width), int(height), presents)


def parse_trees(trees: list[str]):
    return [Tree.parse_tree(t) for t in trees]


def load_file(file):
    with open(file) as f:
        contents = f.read()
        *present_shapes, trees = contents.split("\n\n")
        return parse_present_shapes(present_shapes), parse_trees(trees.split("\n"))
        print(contents)


def main():
    a, b = load_file("input.txt")
    print(a, b)


if __name__ == "__main__":
    main()
