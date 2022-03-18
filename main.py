from bj import blackjack


def main():
    bj = blackjack.Blackjack()
    bj.deal()
    stand = False
    while not bj.bust and not stand:
        for card in bj.player.hand.cards:
            print(card.rank)
            print(card.suit)
            print('===========')
        dec = input('Enter H to hit and S to stand: ')
        print(dec)
        if dec == 'H':
            bj.hit(bj.player)
        elif dec == 'S':
            stand = True
        else:
            print('I did not understand that, try again')
        for card in bj.player.hand.cards:
            print(card.rank)
            print(card.suit)
            print('===========')
    # for card in bj.deck.cards:
    #     print(card.rank)
    #     print(card.suit)
    #     print('===========')
    # bj.deal()
    # print(bj.dealer)
    # print(bj.player.hand)


if __name__ == '__main__':
    main()