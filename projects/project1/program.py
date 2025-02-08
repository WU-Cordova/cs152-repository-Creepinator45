from dataclasses import dataclass
from enum import Enum
from itertools import product, zip_longest
from typing import Iterable, Optional
from datastructures.bag import Bag
from random import choices, randint

class CardSuit(Enum):
    HEARTS = "Hearts"
    CLUBS = "Clubs"
    SPADES = "Spades"
    DIAMONDS = "Diamonds"

class CardFace(Enum):
    ACE = "Ace"
    TWO = "2"
    THREE = "3"
    FOUR = "4"
    FIVE = "5"
    SIX = "6"
    SEVEN = "7"
    EIGHT = "8"
    NINE = "9"
    TEN = "10"
    JACK = "Jack"
    QUEEN = "Queen"
    KING = "King"

@dataclass(frozen=True)
class Card:
    face: CardFace
    suit: CardSuit
    val: int
    def __str__(self) -> str:
        return f"{self.face.value} of {self.suit.value}"

class MultiDeck:
    #generates a single deck of cards, represented as a set, aces are given the value 1 by default
    single_deck = {Card(face = face, suit = suit, val=val) for ((face, val), suit) in product(zip_longest(list(CardFace), range(1,11), fillvalue=10), list(CardSuit))}

    def __init__(self, numDecks:int = 1):
        self.__deck: Bag = Bag(*(list(MultiDeck.single_deck)*numDecks))
    
    def dealCard(self) -> Card:
        """
        Deal a random card from the deck, removing it from the deck and returning the card
        O(n) for cards in deck
        """

        #choice = choices(population = self.__deck.distinct_items(), 
        #                 weights = [self.__deck.count(card_type) for card_type in self.__deck.distinct_items()])
        #return choice
        #I wanted to deal cards using choices with probabilities weighted by the number of each card in the deck, but this isn't working for some reason
        
        choiceIndex = randint(0, len(self.__deck))
        #counts out cards from the deck until reaching the chosen card
        for card in self.__deck.distinct_items():
            choiceIndex -= self.__deck.count(card)
            if choiceIndex <= 0:
                chosenCard = card
                break
        
        self.__deck.remove(chosenCard)
        return chosenCard

class Player:
    def __init__(self, name: str):
        self.__name: str = name
        self.__hand: list[Card] = []
        self.__handValue: int = 0

    def status(self, open: bool = True) -> str:
        """
        return string representation of the player's hand, in the form of "{self.__name}'s hand is {hand}, and the total is {self.__handValue}"
        if open is true will return all cards, if open is false will obscure the first card. Will not include total if open is false
        O(n) for cards in hand
        """
        #I would have used __str__ for this, but I wanted it to be passed the parameter for whether to show or conceal the first card
        #I'm also undecided if I like this function living inside the player class, or if I'd rather define it inside of the beginGame function
        if open:
            hiddenCard = f"{self.__hand[0]} (face down)"
        else:
            hiddenCard = "face down"
        hand = ", ".join([str(card) for card in [hiddenCard] + self.__hand[1:]])

        if open:
            return f"{self.__name}'s hand is {hand}, and the total is {self.__handValue}"
        else:
            return f"{self.__name}'s hand is {hand}"

    @property
    def handValue(self) -> int:
        return self.__handValue
    
    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, name: str) -> None:
        self.__name = name
    
    @property
    def hand(self) -> list[Card]:
        return self.__hand
    
    def calculateHand(hand: Iterable[Card]) -> int:
        """
        Calculates the value of a given hand of 
        O(n) for cards in hand
        """

        containsAce = False
        total = 0
        for card in hand:
            containsAce = containsAce or card.face == CardFace.ACE
            total += card.val
        #Makes aces worth 11 if they fit in the hand
        if containsAce and total <= 11:
            total += 10
        
        return total
    
    def addCard(self, card: Card) -> None:
        """
        Add a given card to the player's hand
        O(n) for cards in hand
        """

        self.__hand.append(card)
        #This could be made O(1) by calculating the new value based on the previous value, instead of recalculating it from scratch
        self.__handValue = Player.calculateHand(self.__hand)
    
    def clearHand(self) -> None:
        self.__hand = []
        self.__handValue = 0


class Game:
    def __init__(self, player1_name:str = "Player", player2_name:str = "Dealer"):
        self.__player1: Player = Player(player1_name)
        self.__player2: Player = Player(player2_name)
    
    def beginGame(self, numDecks: Optional[int] = None) -> None:
        """
        Begins and runs a game of Bag Jack
        """

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
        print(self.__player1.status(open=True))

        self.__player2.addCard(deck.dealCard())
        self.__player2.addCard(deck.dealCard())
        print(self.__player2.status(open=False))
        #todo check for blackjacks

        #player's turn
        print(f"{self.__player1.name}'s turn")
        while True:
            input_choice = input("Hit (h) or Stay (s): ")
            match input_choice:
                case "h":
                    self.__player1.addCard(deck.dealCard())
                    print(self.__player1.status(open=True))

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
        print(self.__player1.status(open=True))

        #CPU's turn
        print(f"{self.__player2.name}'s turn")
        print(self.__player2.status(open=True))
        while self.__player2.handValue < 17:
            print(f"{self.__player2.name} takes a card")
            self.__player2.addCard(deck.dealCard())
            print(self.__player2.status(open=True))

            #exit game if busted
            if self.__player2.handValue > 21:
                print(f"{self.__player2.name} busted. {self.__player1.name} wins!")
                return
        print(f"{self.__player2.name} stays")

        #print the final hands
        print(self.__player1.status(True))
        print(self.__player2.status(True))

        #check for winner
        if self.__player1.handValue > self.__player2.handValue:
            print(f"{self.__player1.name} wins!")
        elif self.__player2.handValue > self.__player1.handValue:
            print(f"{self.__player2.name} wins!")
        else:
            print("Tie!")
        return

def main():
    print("Hello, World!")
    game = Game()
    game.beginGame()

if __name__ == '__main__':
    main()
    pass
