from projects.project1.cardface import CardFace
from projects.project1.cardsuit import CardSuit
from dataclasses import dataclass

@dataclass(frozen=True)
class Card:
    face: CardFace
    suit: CardSuit
    val: int
    def __str__(self) -> str:
        return f"{self.face.value} of {self.suit.value}"
