from ex0.Card import Card
from typing import Union


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, attack: int,
                 health: int) -> None:
        if attack < 0:
            raise ValueError("Attack must be 0 or more")
        if health < 0:
            raise ValueError("Health must be 0 or more")
        super().__init__(name, cost, rarity)
        self.health = health
        self.attack = attack

    def play(self, game_state: dict) -> dict:
        game_state.update({"effect": "Creature summoned to battlefield"})
        return game_state

    def attack_target(self, target: Union["CreatureCard"]) -> dict:
        target.health -= self.attack
        return {
            "attacker": self.name,
            "target": target.name,
            "damage_dealt": self.attack,
            "combat_resolved": True if target.health <= 0 else False
        }

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info.update({"attack": self.attack, "health": self.health})
        return info
