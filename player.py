from game import Game
from deck_dict import val_dict

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

#    def draw(self):
#        """" Prompts the player to hit or stop """
#
#        valid_input = False
#        while valid_input is False:
#            text = input("Would you like to hit? Y/N: ")
#            if text.lower() == "y":
#                self.hand.append(game_deck.pop(0))
#                valid_input = True
#            elif text.lower() == "n":
#                self.stop = True
#            else:
#                print("Invalid Answer")
#        self.game_score = self.hand_calculator()

    def reset(self):
        self.hand = []
        self.stop = False

class Dealer(Player):
    """ Creates a subclass of player for the dealer """

    def __init__(self):
        Player.__init__(self, hidden = True)

#    def draw(self):
#        if self.hand_calculator() < 17:
#            self.hand.append(game_deck.pop(0))
#        else:
#            if "ace" in self.hand: # need to change
#                self.hand.append(game_deck.pop(0))
#            else:
#                self.stop = True
#        self.game_score = self.hand_calculator()
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
