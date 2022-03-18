from hand import Hand

class Player:
    '''represents a player in a game of blackjack'''
    def __init__(self, balance):
        self.balance = balance
        self.hand = Hand()
        