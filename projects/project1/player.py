from projects.project1.card import Card
from projects.project1.cardface import CardFace
from typing import Iterable

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