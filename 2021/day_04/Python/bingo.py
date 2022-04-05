from __future__ import annotations
from dataclasses import dataclass
import os
import __main__
from typing import List, Tuple


class Board:
    def __init__(self, numbers: List[int], row_count: int = 5, column_count: int = 5):
        self.numbers = numbers
        self.row_count = row_count
        self.column_count = column_count
        self.marks = [False for _ in numbers]
        self.bingo = False

    def check_bingo(self, row: int, col: int) -> bool:
        whole_row = self.marks[row * self.column_count : (row + 1) * self.column_count]
        whole_col = self.marks[col::self.row_count]
        if all(whole_row) or all(whole_col):
            self.bingo = True

    def mark(self, number: int):
        try:
            i = self.numbers.index(number)
            self.marks[i] = True
            row = i // self.column_count
            col = i % self.row_count
            self.check_bingo(row, col)
            
        except ValueError:
            pass

    @classmethod
    def from_text(cls, text: str) -> Board:
        numbers = [int(num) for num in text.split()]
        return cls(numbers)

    def score(self, final_call):
        if not self.bingo:
            raise ValueError("No bingo")
        score = 0
        for number, mark in zip(self.numbers, self.marks):
            if mark:
                score += number
        return score * final_call

def find_winner(calls: List[int], boards: List[Board]) -> Tuple[Board, int]:
    for call in calls:
        for board in boards:
            board.mark(call)
            if board.bingo:
                return board, call
    raise ValueError("No winner")

def load_input(path: str) -> Tuple[List[int], List[Board]]:
    filepath = os.path.join(os.path.dirname(__main__.__file__), "..", path)
    with open(filepath) as f:
        text = f.read()
    calls_string, *board_blocks = text.split("\n\n")
    calls = [int(x) for x in calls_string.split(",")]

    boards = [Board.from_text(block) for block in board_blocks]

    return calls, boards

if __name__ == "__main__":
    calls, boards = load_input("input.txt")
    winning_board, final_call = find_winner(calls, boards)
    final_score = winning_board.score(final_call)
    print(final_score)
