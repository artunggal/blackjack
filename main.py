from game import Game
from player import Player, Dealer
from deck_dict import val_dict

deck = list(val_dict)

def main():
    player = Player()
    dealer = Dealer()
    game = Game(player, dealer, deck)
    while game.cont is True:
        game.play_game()
        player.reset()
        dealer.reset()
        game.game_Deck = list(val_dict)
    print("Total Record:")
    print("Wins: ", player.wins)
    print("Losses: ", player.losses)
    print("Pushes/Draws: ", player.pushes)

if __name__ == '__main__':
    main()
