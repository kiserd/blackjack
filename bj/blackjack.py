from player import Player
from deck import Deck

class Blackjack:
    '''simulates a game of blackjack between single player and dealer'''
    def __init__(self):
        self.dealer = Player(0)
        self.player = Player(100)
        self.deck = Deck()
        self.bust = False

    def deal(self):
        '''deal cards to player and dealer'''
        self.deck.shuffle_deck()
        for _ in range(2):
            for player in [self.dealer, self.player]:
                player.hand.add_card(self.deck.deal_card())

    def hit(self, player):
        '''simulates a given player requesting another card'''
        player.hand.add_card(self.deck.deal_card())
        if player.hand.bust:
            self.bust = True