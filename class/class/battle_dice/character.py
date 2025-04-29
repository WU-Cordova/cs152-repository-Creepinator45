from dataclasses import dataclass
from charactertype import CharacterType

@dataclass
class Character:
    name: str
    character_type: CharacterType
    health: int
    attack_power: int