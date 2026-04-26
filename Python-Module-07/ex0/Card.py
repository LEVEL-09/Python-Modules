from abc import ABC, abstractmethod


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        if cost < 0:
            raise ValueError("Cost must be 0 or more")
        self.name = name
        self.cost = cost
        self.rarity = rarity

    def play(self, game_state: dict) -> dict:
        pass
    play = abstractmethod(play)

    def get_card_info(self) -> dict:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity
        }

    def is_playable(self, available_mana: int) -> bool:
        return available_mana >= self.cost
