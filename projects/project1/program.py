from dataclasses import dataclass
from enum import Enum
from itertools import product
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
    def __str__(self) -> str:
        return f"{self.face.value} of {self.suit.value}"

class MultiDeck:
    single_deck = {Card(face = card[0], suit = card[1]) for card in product(list(CardFace), list(CardSuit))}
    def __init__(self, numDecks:int = 1):
        self.__deck: Bag = Bag(*(list(MultiDeck.single_deck)*numDecks))
    
    def dealCard(self) -> Card:
        #choice = choices(population = self.__deck.distinct_items(), 
        #                 weights = [self.__deck.count(card_type) for card_type in self.__deck.distinct_items()])
        #return choice
        #I wanted to deal cards using choices with probabilities weighted by the number of each card in the deck, but this isn't working for some reason
        
        choiceIndex = randint(0, len(self.__deck))
        for card in self.__deck.distinct_items():
            choiceIndex -= self.__deck.count(card)
            if choiceIndex <= 0:
                chosenCard = card
                break
        self.__deck.remove(chosenCard)
        return chosenCard
    
def main():
    print("Hello, World!")



if __name__ == '__main__':
    main()
