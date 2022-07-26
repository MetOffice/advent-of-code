from optparse import check_builtin
import numpy as np
import numpy.ma as ma
from typing import List

class Input:
    """
    Manages the reading of inputs
    """

    @staticmethod
    def read(path):
        """
        Read the input file.
        Returns an array of drawn numbers an a list of 2d arrays of cards.
        """
        with open(path, "r") as file:
            text = file.read()
            
            calls_text, *cards_text = text.split("\n\n")

            calls = Input.read_calls(calls_text)
            cards = [Input.read_card(card_text) for card_text in cards_text]

        return np.array(calls), Cards(cards)

    @staticmethod
    def read_calls(text:str):
        """
        Reads calls
        """
        return [int(call) for call in text.strip().split(",")]

    @staticmethod
    def read_card(card_text:str):
        """
        Reads a card
        """
        numbers = np.array([int(number) for number in card_text.split()])
        return numbers.reshape(5,5)


class Cards:
    """
    Manages the cards
    """
    def __init__(self, cards:np.ndarray):
        cards = np.array(cards)
        self.cards:ma.MaskedArray = ma.masked_array(cards, mask=np.zeros(cards.shape))

    def mark(self, call):
        """
        Mark the call on all cards, returning bingos
        """
        self.cards = ma.masked_equal(self.cards, call)
        return self.check_bingo()

    def check_bingo(self):
        """
        Checks if a card has a bingo, being a row or columnn of all negatives.
        Returns array containing trues for bingos
        """
        # row and column may be reversed but eh
        col_bingo = np.any(np.all(self.cards.mask, axis=1), axis=1) # axis 2 in full array but the array is collapsed by then
        row_bingo = np.any(np.all(self.cards.mask, axis=2), axis=1)
        return col_bingo | row_bingo

    def get_card(self, index):
        return self.cards[index]

class Winner:
    def __init__(self, call, card) -> None:
        self.call = call
        self.card = card

    def __str__(self) -> str:
        return str(self.card) + f"\nScore: {self.score()}"

    def score(self):
        return np.sum(self.card) * self.call

class Game:
    """
    Runs the game
    """
    def __init__(self, calls:np.ndarray, cards:Cards) -> None:
        self.calls = calls
        self.cards = cards

        self.first = None
        self.last = None

    def call(self, number:int):
        return self.cards.mark(number)

    def play(self):
        """
        Call each number in turn, marking off numbers
        Record the first card to say bingo and the last
        """
        bingos = self.cards.check_bingo()
        previous_bingos = bingos
        for number in self.calls:
            bingos = self.call(number)
            self.spot_first_bingo(number, bingos)
            self.spot_last_bingo(number, bingos, previous_bingos)
            previous_bingos = bingos
            if self.game_over():
                break
        self.announce()

    def spot_first_bingo(self, call, bingos):
        if self.first is not None:
            return
        if np.any(bingos):
            self.first = Winner(call, self.cards.get_card(bingos))

    def spot_last_bingo(self, call, bingos, previous_bingos):
        if self.last is not None:
            return
        if np.all(bingos):
            last_bingos = bingos ^ previous_bingos
            self.last = Winner(call, self.cards.get_card(last_bingos))

    def game_over(self):
        return self.first is not None and self.last is not None

    def announce(self):
        print("First winner:")
        print(self.first)
        print("Last winner:")
        print(self.last)

path = "./2021/day_04/input.txt"
game = Game(*Input.read(path))
game.play()