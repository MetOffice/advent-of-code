"""
A button: 3 tokens
B button: 1 token

If we assume there's only one valid number of A&B presses,
let's just find out what that is
"""

from dataclasses import dataclass
import numpy as np
import re


@dataclass
class ClawMachine:
    a: np.ndarray
    b: np.ndarray
    prize: np.ndarray


BUTTON_REGEX = re.compile(r"Button [AB]: X\+(?P<x>\d+), Y\+(?P<y>\d+)\n")


def read_xy(input: list[str], regex: re.Pattern[str]) -> tuple[np.ndarray, list[str]]:
    line, *rest = input
    m = regex.fullmatch(line)
    assert m
    return np.array([int(m.group("x")), int(m.group("y"))]), rest


PRIZE_REGEX = re.compile(r"Prize: X=(?P<x>\d+), Y=(?P<y>\d+)\n")


def read_claw_machine(input: list[str]) -> tuple[ClawMachine, list[str]]:
    a, rest = read_xy(input, BUTTON_REGEX)
    b, rest = read_xy(rest, BUTTON_REGEX)
    prize, rest = read_xy(rest, PRIZE_REGEX)
    if rest:
        _, *rest = rest
    return ClawMachine(a, b, prize), rest


def read_input(path: str):
    with open(path) as f:
        lines = list(f.readlines())

    claw_machines: list[ClawMachine] = []
    while lines:
        claw_machine, lines = read_claw_machine(lines)
        claw_machines.append(claw_machine)
