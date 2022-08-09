
import numpy as np

segments = "abcdefg"

template = [
" aaaaa ",
"b     c",
"b     c",
"b     c",
" ddddd ",
"e     f",
"e     f",
"e     f",
" ggggg "
]

display_character = (" ", "#")

def add_blank_digit(line):
    """
    Adds a new blank digit to end of current line
    """
    if all(line):
        # concat template to end of existing line
        return [f"{line_row} {template_row}" for line_row, template_row in zip(line, template)]
    else:
        # new line with one digit
        return template

def shade_blank_digit(line, digit):
    """
    Shades the blank digit at the end of a line according to digit list
    """
    return [shade_row(row, digit) for row in line]

def shade_row(row, digit):
    """
    Shade a single row
    """
    for segment, active in zip(segments, digit):
        row = row.replace(segment, display_character[active])
    return row

def display(digits:np.ndarray):
    """
    Display an array of digits
    """
    # arbitrary collection with all elements = false
    line = [0]

    # wrap single digits into one character line
    if len(digits.shape) == 1:
        digits = np.expand_dims(digits, 0)

    assert len(digits.shape) == 2, "Incorrect number of dimensions, must be 1d or 2d array."

    for digit in digits:
        line = add_blank_digit(line)
        line = shade_blank_digit(line, digit)

    for row in line:
        print(row)