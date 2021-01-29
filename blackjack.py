# code for a game of blackjack/21

import random

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
game_deck = deck

# create a ___ where i can pop the top item after randomizing

class Game:
    def __init__(self, player, dealer):
        self.player = player
        self.dealer = dealer
        self.cont = True

    def play_game(self):
        """ Plays a round of blackjack """
        # give two cards to a player
        # after each round, cards are reshuffled
        random.shuffle(game_deck)
        #self.deck = deck
        for i in range(2):
            self.player.hand.append(game_deck.pop(0))
            self.dealer.hand.append(game_deck.pop(0))
        self.player.game_score = self.player.hand_calculator()
        self.dealer.game_score = self.dealer.hand_calculator(end = True)

        # do all of the player moves until self.player.stop == True
        while self.player.stop == False:
            print("Player Hand: ", self.player.hand)
            #for card in self.player.hand:
            #    print(card)
            print("Player Score: ", self.player.game_score)
            if self.player.game_score >= 21:
                self.dealer.stop = True
                self.player.stop = True
                break
            self.player.draw()

        # then show dealer's second hand
        while self.dealer.stop == False:
            print("Dealer Hand: ", self.dealer.hand)
            #for card in self.dealer.hand:
            #    print(card)
            print("Dealer Score: ", self.dealer.game_score)
            if self.dealer.game_score >= 21:
                self.dealer.stop = True
                break
            self.dealer.draw()

        # compare scores and award
        # fix scoring to take into account 21

        # instances where players bust - automatic loss
        if self.player.game_score > 21:
            print("Dealer wins (Player busts)")
            self.dealer.wins += 1
            self.player.losses += 1
        # instance where dealer busts - loss only if player doesn't bust
        elif self.dealer.game_score > 21:
            print("Player wins (Dealer busts)")
            self.player.wins += 1
            self.dealer.losses += 1
        # instance where player gets blackjack - win if dealer
        # doesn't get blackjack
        elif self.player.game_score == 21:
            if self.deaer.game_score == 21:
                print("Push (Both parties have a blackjack)")
                self.player.pushes += 1
                self.dealer.pushes += 1
            else:
                print("Player wins with a blackjack")
                self.player.wins += 1
                self.dealer.losses += 1
        # instance where dealer gets blackjack - win if player doesn't
        # get blackjack
        elif self.dealer.game_score == 21:
            print("Dealer wins with a blackjack")
            self.dealer.wins += 1
            self.player.losses += 1

        else:
            if self.dealer.game_score > self.player.game_score:
                print("Dealer wins!")
                self.dealer.wins += 1
                self.player.losses += 1
            if self.dealer.game_score < self.player.game_score:
                print("Player wins!")
                self.player.wins += 1
                self.dealer.losses += 1
            if self.dealer.game_score == self.player.game_score:
                print("Push (Same score)")
                self.player.pushes += 1
                self.dealer.pushes += 1

        valid_input = False
        while valid_input is False:
            text = input("Would you like to play again? Y/N: ")
            if text.lower() == "y":
                valid_input = True
            elif text.lower() == "n":
                self.cont = False
                valid_input = True
            else:
                print("Invalid Answer")
        return

    # take note the rule on splitting

class Player(Game):
    """Creates a class for a general player"""

    def __init__(self, hand = None, game_score = 0, wins = 0, losses = 0,
                pushes = 0, hidden = False):
        if hand == None:
            self.hand = []
        self.game_score = game_score
        self.wins = wins
        self.losses = losses
        self.pushes = pushes
        self.stop = False
        self.hidden = hidden

    def hand_calculator(self):
        summ = 0
        ace_count = 0
        for card in self.hand:
            to_add = val_dict[card]
            if "ace" in card:
                ace_count += 1
            summ += to_add
        if ace_count > 0:
            if summ + 10 <= 21:
                summ = summ + 10
        return summ

    def draw(self):
        """" Prompts the player to hit or stop """

        valid_input = False
        while valid_input is False:
            text = input("Would you like to hit? Y/N: ")
            if text.lower() == "y":
                self.hand.append(game_deck.pop(0))
                valid_input = True
            elif text.lower() == "n":
                self.stop = True
                valid_input = True
            else:
                print("Invalid Answer")
        self.game_score = self.hand_calculator()

    def reset(self):
        self.hand = []
        self.stop = False

class Dealer(Player):
    """ Creates a subclass of player for the dealer """

    def __init__(self):
        Player.__init__(self, hidden = True)

    def draw(self):
        if self.hand_calculator() < 17:
            self.hand.append(game_deck.pop(0))
        else:
            if "ace" in self.hand: # need to change
                self.hand.append(game_deck.pop(0))
            else:
                self.stop = True
        self.game_score = self.hand_calculator()
        # some algorithm

    def hand_calculator(self, end = True):
        summ = 0
        ace_count = 0
        if end == False:
            for i in range(len(self.hand) - 1):
                to_add = val_dict[self.hand[i]]
                if "ace" in self.hand[i]:
                    ace_count += 1
                summ += to_add
            if ace_count > 0:
                if summ + 10 <= 21:
                    return summ + 10
        if end == True:
            for card in self.hand:
                to_add = val_dict[card]
                if "ace" in card:
                    ace_count += 1
                summ += to_add
            if ace_count > 0:
                if summ + 10 <= 21:
                    summ = summ + 10
            return summ

# get prompt
# if yes: draw; if no, keep hand

#def draw():
    # card = game_Deck.pop(0)

def main():
    player = Player()
    dealer = Dealer()
    game = Game(player, dealer)
    while game.cont is True:
        game.play_game()
        player.reset()
        dealer.reset()
        game_deck = deck
    print("Total Record:")
    print("Wins: ", player.wins)
    print("Losses: ", player.losses)
    print("Pushes/Draws: ", player.pushes)

if __name__ == '__main__':
    main()
