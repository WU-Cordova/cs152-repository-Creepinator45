from projects.project1.card import Card
from projects.project1.cardface import CardFace
from typing import Iterable

class Player:
    def __init__(self, name: str):
        self.__name: str = name
        self.__hand: list[Card] = []
        self.__handValue: int = 0

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