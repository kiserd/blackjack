
class Hand:
    """represents a hand in blackjack"""
    def __init__(self):
        """initializes player hand to empty"""
        self.cards = []
        self.soft_score = 0
        self.hard_score = 0
        self.score = 0
        self.has_ace = False
        self.bust = False

    def add_card(self, card):
        """adds card to hand, either from a hit or new deal"""
        self.cards.append(card)
        # handle score update
        self.soft_score += card.soft
        self.hard_score += card.hard
        # check for bust and calculate score
        self.calc_score()

    def calc_score(self):
        """update score fields"""
        if self.hard_score > 21:
            self.bust = True
        # determine score to keep
        if self.soft_score > 21:
            self.score = self.hard_score
        else:
            self.score = self.soft_score

    def print_dealer(self):
        print('Dealer: ')
        print(f'|{self.cards[0].rank}|')
        print('=============')

    def __str__(self):
        s = f'score: {int(self.soft_score)}, {int(self.hard_score)}'
        s += '  '
        for card in self.cards:
            s += f'|{card.rank}| '
        return s[:-1]
