from bj.player import Player
from bj.deck import Deck


class Blackjack:
    """simulates a game of blackjack between single player and dealer"""
    def __init__(self):
        self.dealer = Player(0)
        self.player = Player(100)
        self.deck = Deck()
        self.bet = 0
        self.player_win = None

    def play(self):
        playing = True
        while playing:
            print(f'Balance: ${self.player.balance}')
            self.get_bet()
            self.deal()
            self.dealer.hand.print_dealer()
            print(self.player.hand)
            self.proposition_player()
            # handle dealer
            if self.player.hand.bust:
                print('Dealer: ')
                print(self.dealer.hand)
                return 1
            self.play_dealer()
            print('Dealer: ')
            print(self.dealer.hand)
            self.calc_score()
            self.settle_funds()
            decision = None
            while decision != 'q' and decision != 'c':
                decision = input('q to quit and c to continue: ')
                if decision == 'q':
                    playing = False

    def proposition_player(self):
        stand = False
        while not self.player.hand.bust and not stand:
            dec = input('Enter H to hit and S to stand: ')
            if dec == 'H':
                self.hit(self.player)
            elif dec == 'S':
                stand = True
            else:
                print('I did not understand that, try again')
            print(self.player.hand)
            # handle case of bust
            if self.player.hand.bust:
                print('sorry, you busted')
            print('============')

    def deal(self):
        """deal cards to player and dealer"""
        for p in [self.dealer, self.player]:
            p.clear_hand()
        self.deck.shuffle_deck()
        for _ in range(2):
            for player in [self.dealer, self.player]:
                player.hand.add_card(self.deck.get_card())
        # reset player_win indicator
        self.player_win = None

    def hit(self, player):
        """simulates a given player requesting another card"""
        player.hit(self.deck.get_card())

    def play_dealer(self):
        """
        simulates dealer play
        stand on soft/hard 17
        """
        while self.dealer.hand.soft_score < 17 and not self.dealer.hand.bust:
            self.hit(self.dealer)
            print(self.dealer.hand)

    def calc_score(self):
        """determines winner of hand"""
        # handle case of player bust
        if self.player.hand.bust:
            self.player_win = False
        # handle case of dealer bust
        elif self.dealer.hand.bust:
            self.player_win = True
        # handle case of no busts
        else:
            if self.player.hand.score > self.dealer.hand.score:
                self.player_win = True
            elif self.dealer.hand.score > self.player.hand.score:
                self.player_win = False

    def settle_funds(self):
        if self.player_win:
            self.player.balance += (self.bet * 2)
        elif self.player_win is None:
            self.player.balance += self.bet
        self.bet = 0

    def get_bet(self):
        """gets wager from player and updates properties"""
        valid_bet = False
        while not valid_bet:
            try:
                wager = int(input('Please enter a bet: $'))
            except:
                print('Sorry, that bet was not valid')
            else:
                if wager > self.player.balance:
                    print('You do not have enough $ to place that bet')
                else:
                    self.bet = wager
                    self.player.balance -= wager
                    valid_bet = True



