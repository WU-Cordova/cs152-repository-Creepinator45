from projects.project1.player import Player
from projects.project1.multideck import MultiDeck
from typing import Optional
from random import randint

class Game:
    def __init__(self, player1_name:str = "Player", player2_name:str = "Dealer"):
        self.__player1: Player = Player(player1_name)
        self.__player2: Player = Player(player2_name)
    
    def beginGame(self, numDecks: Optional[int] = None) -> None:
        """
        Begins and runs a game of Bag Jack
        """

        #function for formatting a given player's hand for printing
        def player_status(player: Player, open: bool = True) -> str:
            """
            return string representation of the player's hand, in the form of "{self.__name}'s hand is {hand}, and the total is {self.__handValue}"
            if open is true will return all cards, if open is false will obscure the first card. Will not include total if open is false
            O(n) for cards in hand
            """
            if open:
                hiddenCard = f"{player.hand[0]} (face down)"
            else:
                hiddenCard = "face down"
            hand = ", ".join([str(card) for card in [hiddenCard] + player.hand[1:]])

            if open:
                return f"{player.name}'s hand is {hand}, and the total is {player.handValue}"
            else:
                return f"{player.name}'s hand is {hand}"

        #setting up the game
        self.__player1.clearHand()
        self.__player2.clearHand()

        #randomly selects number of decks from 2, 4, 6, and 8 if none is supplied
        if numDecks is None:
            numDecks = 2 * randint(1, 4)

        deck = MultiDeck(numDecks=numDecks)

        print(f"{self.__player1.name} is playing Bag Jack against {self.__player2.name}. Dealing from {numDecks} decks")

        #drawing starting hands
        self.__player1.addCard(deck.dealCard())
        self.__player1.addCard(deck.dealCard())
        print(player_status(self.__player1, open=True))

        self.__player2.addCard(deck.dealCard())
        self.__player2.addCard(deck.dealCard())
        print(player_status(self.__player2, open=False))
        #todo check for blackjacks

        #player's turn
        print(f"{self.__player1.name}'s turn")
        while True:
            input_choice = input("Hit (h) or Stay (s): ")
            match input_choice:
                case "h":
                    self.__player1.addCard(deck.dealCard())
                    print(player_status(self.__player1, open=True))

                    #exit game if busted
                    if self.__player1.handValue > 21:
                        print(f"{self.__player1.name} busted. {self.__player2.name} wins!")
                        return
                    #end turn if 21
                    if self.__player1.handValue == 21:
                        break
                    continue
                case "s":
                    #end turn
                    break
                case _:
                    #ask for input again if not give "h" or "s"
                    print(f"{input_choice} was not a valid decision")
                    continue
        print(player_status(self.__player1, open=True))

        #CPU's turn
        print(f"{self.__player2.name}'s turn")
        print(player_status(self.__player2, open=True))
        while self.__player2.handValue < 17:
            print(f"{self.__player2.name} takes a card")
            self.__player2.addCard(deck.dealCard())
            print(player_status(self.__player2, open=True))

            #exit game if busted
            if self.__player2.handValue > 21:
                print(f"{self.__player2.name} busted. {self.__player1.name} wins!")
                return
        print(f"{self.__player2.name} stays")

        #print the final hands
        print(player_status(self.__player1, open=True))
        print(player_status(self.__player2, open=True))

        #check for winner
        if self.__player1.handValue > self.__player2.handValue:
            print(f"{self.__player1.name} wins!")
        elif self.__player2.handValue > self.__player1.handValue:
            print(f"{self.__player2.name} wins!")
        else:
            print("Tie!")
        return

    def beginGames(self) -> None:
        """
        Plays bagjack with a random number of decks and offers a rematch until the player declines
        """

        print("Let's play some Bag Jack!")
        play_again = True
        while play_again:
            #Play a single game of bagjack
            self.beginGame()
            #Ask for a rematch
            while True:
                input_choice = input("Would you like to play again? (y/n):")
                match input_choice:
                    case "y":
                        break
                    case "n":
                        play_again = False
                        break
                    case _:
                        print(f"{input_choice} was not a valid decision")
        print("Thanks for playing!")