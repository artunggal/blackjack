import random

class Game:
    def __init__(self, player, dealer, start_Deck, game_Deck):
        self.player = player
        self.dealer = dealer
        self.cont = True
        self.start_Deck = start_Deck
        self.game_Deck = game_Deck

    def play_game(self):
        """ Plays a round of blackjack """
        # give two cards to a player
        # after each round, cards are reshuffled
        random.shuffle(self.game_Deck)
        #self.game_Deck = deck
        for i in range(2):
            self.player.hand.append(self.game_Deck.pop(0))
            self.dealer.hand.append(self.game_Deck.pop(0))
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
            else:
                self.draw("player")

        # then show dealer's second hand
        while self.dealer.stop == False:
            print("Dealer Hand: ", self.dealer.hand)
            #for card in self.dealer.hand:
            #    print(card)
            print("Dealer Score: ", self.dealer.game_score)
            if self.dealer.game_score >= 21:
                self.dealer.stop = True
                break
            self.draw("dealer")

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
            if self.dealer.game_score == 21:
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
                self.game_Deck = game_deck
            elif text.lower() == "n":
                self.cont = False
                valid_input = True
            else:
                print("Invalid Answer")
        return

    def draw(self, player_type):
        if player_type == "player":
            valid_input = False
            while valid_input is False:
                text = input("Would you like to hit? Y/N: ")
                if text.lower() == "y":
                    self.player.hand.append(self.game_Deck.pop(0))
                    valid_input = True
                elif text.lower() == "n":
                    self.player.stop = True
                    valid_input = True
                else:
                    print("Invalid Answer")
            self.player.game_score = self.player.hand_calculator()
        else:
            if self.dealer.hand_calculator() < 17:
                self.dealer.hand.append(self.game_Deck.pop(0))
            else:
                if "ace" in self.dealer.hand: # need to change
                    self.dealer.hand.append(self.game_Deck.pop(0))
                else:
                    self.dealer.stop = True
            self.dealer.game_score = self.dealer.hand_calculator()
    # take note the rule on splitting

    # take note the rule on splitting
