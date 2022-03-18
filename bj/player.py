from bj.hand import Hand


class Player:
    """represents a player in a game of blackjack"""
    def __init__(self, balance):
        self.balance = balance
        self.hand = Hand()

    def hit(self, card):
        """simulates a given player requesting another card"""
        self.hand.add_card(card)

    def clear_hand(self):
        self.hand = Hand()

class Dealer(Player):
    """represents a dealer in a game of blackjack"""

        