# helper dict to determine value from rank
vals = {
    '2': [2, 2],
    '3': [3, 3],
    '4': [4, 4],
    '5': [5, 5],
    '6': [6, 6],
    '7': [7, 7],
    '8': [8, 8],
    '9': [9, 9],
    '10': [10, 10],
    'J': [10, 10],
    'Q': [10, 10],
    'K': [10, 10],
    'A': [1, 11]
}


class Card:
    """
    represents a card in a typical 52-card deck of playing cards
    """
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.soft = vals[rank][1]
        self.hard = vals[rank][0]
