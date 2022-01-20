
def read_input():
    with open("./2020/day_22/input.txt", "r") as file:
        lines = file.readlines()
    return lines

def play_combat():
    """
    Set up two decks, have them play combat and return the score of the winner
    """
    # set up both decks
    my_deck, crab_deck = initialise_decks()
    # play while both decks have cards
    while my_deck.any() and crab_deck.any():
        my_card = my_deck.draw()
        crab_card = crab_deck.draw()
        # if I win, I gain both cards
        if my_card > crab_card:
            my_deck.gain(my_card, crab_card)
        # otherwise crab wins
        else:
            crab_deck.gain(crab_card, my_card)
    # if I still have cards i win
    if my_deck.any():
        return my_deck.score()
    else:
        return crab_deck.score()

def play_recursive_combat():
    """
    Set up two decks, have them play recursive combat and return the score of the winner
    """
    # set up both decks
    my_deck, crab_deck = initialise_decks()
    # Play the recursive combat
    victor, score = resolve_recursive_combat(my_deck, crab_deck)
    return score
    
def resolve_recursive_combat(my_deck, crab_deck):
    """
    Resolve a game of recursive combat, returning the victor and their score
    """
    # Remember previous states of the game
    past = []
    # play while both decks have cards
    while my_deck.any() and crab_deck.any():
        # record the state of this game as a hash of our decks
        state = hash((my_deck, crab_deck))
        # if we are in a previous state, I win
        if state in past:
            return True, my_deck.score()
        # otherwise record the current state
        else:
            past.append(state)
        # draw cards
        my_card = my_deck.draw()
        crab_card = crab_deck.draw()
        # if our decks are both sufficiently long, we recurse
        if my_card <= len(my_deck) and crab_card <= len(crab_deck):
            # new game with top cards of our decks
            victor, _ = resolve_recursive_combat(my_deck.subdeck(my_card), crab_deck.subdeck(crab_card))
        # otherwise choose winner as normal
        else:
            victor = my_card > crab_card
        # if I win, I gain both cards
        if victor:
            my_deck.gain(my_card, crab_card)
        # otherwise crab wins
        else:
            crab_deck.gain(crab_card, my_card)
    # if I still have cards i win
    if my_deck.any():
        return True, my_deck.score()
    else:
        return False, crab_deck.score()

def initialise_decks():
    """
    Read the input file and create two decks based on its contents
    """
    # create lists for both decks
    my_cards = []
    crab_cards = []
    # create iterator for consistent line reads
    lines = iter(read_input())
    # fill my deck first
    for line in lines:
        # if line break swap to crab deck
        if line == "\n":
            break
        # otherwise attempt to add it if it is a card
        else:
            try:
                card = int(line)
                my_cards.append(card)
            # if it says player 1 or smt don't bother
            except:
                pass
    # same for crab
    for line in lines:
        if line == "\n":
            break
        else:
            try:
                card = int(line)
                crab_cards.append(card)
            except:
                pass
    # return two decks
    return Deck(my_cards), Deck(crab_cards)

class Deck():
    """
    Holds cards in a deck and allows useful manipulations
    """
    def __init__(self, cards:list):
        self.cards = cards

    def __eq__(self, other):
        """
        Two decks are equal if they contain the same cards in the same order
        Need to implement for hash
        """
        return all([pair[0] == pair[1] for pair in zip(self.cards, other.cards)])

    def __hash__(self):
        """
        Return a hash of the cards in a deck. Different decks almost certainly have different hashes
        """
        return hash(tuple(self.cards))

    def __len__(self):
        """
        The length of a deck is the length of ts card list
        """
        return len(self.cards)

    def draw(self):
        """
        Draw a single card, removing it from the deck
        """
        return self.cards.pop(0)

    def any(self):
        """
        Return true if there are any cards in the deck, else false
        """
        return len(self.cards) > 0

    def gain(self, *cards):
        """
        Add all given cards to the bottom of the deck
        """
        self.cards += cards

    def subdeck(self, x):
        """
        Create a new deck copying the top x cards of this deck
        """
        return Deck(self.cards[:x])
    
    def score(self):
        """
        Return the score of the deck
        """
        total = 0
        # enumerate in backwards order, as cards at the bottom are worth least and cards at the top the most
        for i, card in enumerate(self.cards[::-1]):
            # add 1 for zero-ordering
            total += (i + 1) * card
        return total

if __name__ == "__main__":
    print(play_recursive_combat())