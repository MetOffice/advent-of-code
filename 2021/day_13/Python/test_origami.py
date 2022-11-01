import pytest

from origami import *

SAMPLE_COORDS = [
    (6, 10),
    (0, 14),
    (9, 10),
    (0, 3),
    (10, 4),
    (4, 11),
    (6, 0),
    (6, 12),
    (4, 1),
    (0, 13),
    (10, 12),
    (3, 4),
    (3, 0),
    (8, 4),
    (1, 10),
    (2, 14),
    (8, 10),
    (9, 0),
]


@pytest.mark.parametrize(
    ("coords", "axis", "value", "expected_coords"),
    [
        (
            SAMPLE_COORDS,
            "y",
            7,
            [
                (0, 0),
                (0, 1),
                (0, 3),
                (1, 4),
                (2, 0),
                (3, 0),
                (3, 4),
                (4, 1),
                (4, 3),
                (6, 0),
                (6, 2),
                (6, 4),
                (8, 4),
                (9, 0),
                (9, 4),
                (10, 2),
                (10, 4),
            ],
        )
    ],
)
def test_apply_single_fold(coords, axis, value, expected_coords):
    x_list = [coord[0] for coord in coords]
    y_list = [coord[1] for coord in coords]
    paper = Paper(x_list, y_list)
    paper.apply_single_fold((axis, value))
    assert set(zip(paper.x_list, paper.y_list)) == set(expected_coords)


def test_paper_str():
    coords = [(0, 0), (0, 1), (0, 3), (1, 4), (2, 0), (3, 0)]
    x_list = [coord[0] for coord in coords]
    y_list = [coord[1] for coord in coords]
    paper = Paper(x_list, y_list)
    expected = """# ##
#   
    
#   
 #  """
    assert str(paper) == expected
