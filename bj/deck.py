import random
from bj.card import Card
# helpers for building out deck of cards
suits = ['diamonds', 'clubs', 'hearts', 'spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']


class Deck:
    """represents a deck of 52 playing cards"""
    def __init__(self):
        """
        initializes deck of cards as expected
        """
        # populate deck and give them an init shuffle
        self.cards = [Card(s, r) for s in suits for r in ranks]
        random.shuffle(self.cards)
        # define housekeeping fields
        self.next_idx = -1

    def get_card(self):
        """
        simulates generating a card from the top of the deck
        """
        # handle case where all 52-cards have been dealt
        if self.next_idx == -53:
            print('something went wrong, all cards have been dealt already')
            return None
        # handle case where card is available
        next_card = self.cards[self.next_idx]
        self.next_idx += 1
        return next_card

    def shuffle_deck(self):
        """
        shuffles deck of cards and returns next index pointer to top of deck
        """
        self.next_idx = -1
        random.shuffle(self.cards)
