
class Hand:
    '''represents a hand in blackjack'''
    def __init__(self):
        '''initializes player hand to empty'''
        self.cards = []
        self.soft_score = 0
        self.hard_score = 0
        self.has_ace = False
        self.bust = False

    def add_card(self, card):
        '''adds card to hand, either from a hit or new deal'''
        self.cards.append(card)
        # handle addition of an ace
        if card.rank == 'A':
            self.has_ace = True
            self.soft_score += card.val[1]
            self.hard_score += card.val[0]
        # handle all other cards
        else:
            self.soft_score += card.val
            self.hard_score += card.val
        # handle bust
        if self.hard_score > 21:
            self.bust = True

    # def print_dealer(self):
    #     print(f'|{self.cards[0].rank}|')

    # def __str__(self):
    #     s = f'score: {int(self.hard_score)}'
    #     if self.has_ace:
    #         s += f', {int(self.soft_score)}'
    #     s += '  '
    #     for card in self.cards:
    #         s += f'|{card.rank}| '
    #     return s[:-1]
