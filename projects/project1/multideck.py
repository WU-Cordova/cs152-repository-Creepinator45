from projects.project1.card import Card
from projects.project1.cardface import CardFace
from projects.project1.cardsuit import CardSuit
from datastructures.bag import Bag
from random import randint
from itertools import product, zip_longest

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
