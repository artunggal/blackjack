from game import Game
from player import Player, Dealer

# create dictionary of values
val_dict = {
  "ace_Clubs": 1,
  "two_Clubs": 2,
  "three_Clubs": 3,
  "four_Clubs": 4,
  "five_Clubs": 5,
  "six_Clubs": 6,
  "seven_Clubs": 7,
  "eight_Clubs": 8,
  "nine_Clubs": 9,
  "ten_Clubs": 10,
  "jack_Clubs": 10,
  "queen_Clubs": 10,
  "king_Clubs": 10,

  "ace_Spades": 1,
  "two_Spades": 2,
  "three_Spades": 3,
  "four_Spades": 4,
  "five_Spades": 5,
  "six_Spades": 6,
  "seven_Spades": 7,
  "eight_Spades": 8,
  "nine_Spades": 9,
  "ten_Spades": 10,
  "jack_Spades": 10,
  "queen_Spades": 10,
  "king_Spades": 10,

  "ace_Hearts": 1,
  "two_Hearts": 2,
  "three_Hearts": 3,
  "four_Hearts": 4,
  "five_Hearts": 5,
  "six_Hearts": 6,
  "seven_Hearts": 7,
  "eight_Hearts": 8,
  "nine_Hearts": 9,
  "ten_Hearts": 10,
  "jack_Hearts": 10,
  "queen_Hearts": 10,
  "king_Hearts": 10,

  "ace_Diamonds": 1,
  "two_Diamonds": 2,
  "three_Diamonds": 3,
  "four_Diamonds": 4,
  "five_Diamonds": 5,
  "six_Diamonds": 6,
  "seven_Diamonds": 7,
  "eight_Diamonds": 8,
  "nine_Diamonds": 9,
  "ten_Diamonds": 10,
  "jack_Diamonds": 10,
  "queen_Diamonds": 10,
  "king_Diamonds": 10
}

deck = list(val_dict)

def main():
    player = Player()
    dealer = Dealer()
    game = Game(player, dealer, deck, deck)
    while game.cont is True:
        game.play_game()
        player.reset()
        dealer.reset()
        game.game_Deck = game.start_Deck
    print("Total Record:")
    print("Wins: ", player.wins)
    print("Losses: ", player.losses)
    print("Pushes/Draws: ", player.pushes)

if __name__ == '__main__':
    main()
