from ex0.Card import Card
from ex2.Combatable import Combatable
from .Rankable import Rankable
import random


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name: str, card_id: str, cost: int,
                 rarity: str, value_attack: int, value_health: int) -> None:
        if value_attack < 0:
            raise ValueError("Attack must be 0 or more")
        if value_health < 0:
            raise ValueError("Health must be 0 or more")
        if cost < 0:
            raise ValueError("Cost must be 0 or more")
        super().__init__(name, cost, rarity)
        self.card_id = card_id
        self.wins = 0
        self.losses = 0
        self.rating = 0
        self.value_attack = value_attack
        self.value_health = value_health
        self.rating = random.randint(1, 5000)
        self.combat = "Cry"

    def play(self, game_state: dict) -> dict:
        return game_state

    def attack(self, target) -> dict:
        target.value_health -= self.value_attack
        return {
            "attacker": self.card_id,
            "target": target.card_id,
        }

    def defend(self, incoming_damage: int) -> dict:
        shield = int(incoming_damage/2)
        self.value_health += shield
        return {
            "MERCY": shield
        }

    def get_combat_stats(self) -> dict:
        return {
            "Combat": self.combat
        }

    def calculate_rating(self) -> int:
        return self.rating

    def update_wins(self, wins: int) -> None:
        self.wins += 1

    def update_losses(self, losses: int) -> None:
        self.losses += 1

    def get_rank_info(self) -> dict:
        return {
            "Rating": self.calculate_rating(),
        }

    def get_tournament_stats(self) -> dict:
        return {
            "Interfaces": [cls.__name__ for cls in
                           TournamentCard.__mro__[1:4]],
            "Rating": self.calculate_rating(),
            "Record": f"{self.wins}-{self.losses}"
        }
