from .CardFactory import CardFactory
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex0.main import Rarity
from typing import Any, Dict
import random


class FantasyCardFactory(CardFactory):
    creatures = [
            {"name": "Dragons", "cost": 6, "rarity": Rarity.L.value,
             "attack": 8, "health": 6},
            {"name": "Goblins", "cost": 3, "rarity": Rarity.C.value,
             "attack": 4,
             "health": 2},
            {"name": "Frost Mage", "cost": 4,
             "rarity": Rarity.R.value, "attack": 3,
             "health": 5},
            {"name": "Thunder Spirit", "cost": 2, "rarity": Rarity.U.value,
             "attack": 3, "health": 2},
            {"name": "Iron Guardian", "cost": 7,
             "rarity": Rarity.R.value, "attack": 6,
             "health": 9},
            {"name": "Night Stalker", "cost": 3, "rarity": Rarity.U.value,
             "attack": 5,
             "health": 3},
            {"name": "Radiant Seraph", "cost": 5, "rarity": Rarity.R.value,
             "attack": 3,
             "health": 7},
            {"name": "Woodland Pixie", "cost": 1, "rarity": Rarity.C.value,
             "attack": 1,
             "health": 2},
    ]

    spells = [
        {"name": "Thunder Strike", "cost": 3, "rarity": Rarity.C.value,
         "effect_type":
         "damage"},
        {"name": "Fire", "cost": 2, "rarity": Rarity.C.value, "effect_type":
         "heal"},
        {"name": "Flame Burst", "cost": 4,
         "rarity": Rarity.U.value, "effect_type":
         "damage"},
        {"name": "Barrier Charm", "cost": 1,
         "rarity": Rarity.C.value, "effect_type":
         "buff"},
        {"name": "Ice", "cost": 7, "rarity": Rarity.L.value, "effect_type":
         "damage"},
        {"name": "Lightning", "cost": 2,
         "rarity": Rarity.C.value, "effect_type":
         "damage"},
        {"name": "Holy Radiance", "cost": 5,
         "rarity": Rarity.R.value, "effect_type":
         "heal"},
        {"name": "Arcane Shot", "cost": 1,
         "rarity": Rarity.C.value, "effect_type":
         "damage"},
    ]

    artifacts = [
        {"name": "Rings", "cost": 2, "rarity": Rarity.C.value, "durability": 4,
         "effect": "Permanent: +1 mana regeneration"},
        {"name": "Staffs", "cost": 4, "rarity": Rarity.U.value,
         "durability": 3,
         "effect": "Permanent: +3 attack to equipped creature"},
        {"name": "Crystals", "cost": 5, "rarity": Rarity.R.value,
         "durability": 5,
         "effect": "Permanent: Draw one extra card every two turns"},
        {"name": "Guardian Shield", "cost": 4, "rarity": Rarity.R.value,
         "durability": 6, "effect": "Permanent: +2 health to all allies"},
        {"name": "Emperor's Crown", "cost": 8, "rarity": Rarity.L.value,
         "durability": 9,
         "effect": "Permanent: All cards cost 1 less"},
        {"name": "Swift Boots", "cost": 2, "rarity": Rarity.U.value,
         "durability": 2, "effect": "Permanent: Creatures gain haste"},
        {"name": "Veil Cloak", "cost": 3, "rarity": Rarity.U.value,
         "durability": 4,
         "effect": "Permanent: Creatures gain stealth"},
        {"name": "Elemental Rod", "cost": 6, "rarity": Rarity.L.value,
         "durability": 7, "effect": "Permanent: +2 spell power"},
    ]

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        random_data: Dict[str, Any] = random.choice(self.creatures)
        if isinstance(name_or_power, str):
            return CreatureCard(
                name_or_power,
                random_data["cost"],
                random_data["rarity"],
                random_data["attack"],
                random_data["health"]
            )
        elif isinstance(name_or_power, int):
            return CreatureCard(
                random_data["name"],
                random_data["cost"],
                random_data["rarity"],
                name_or_power,
                random_data["health"]
            )
        return CreatureCard(
            random_data["name"],
            random_data["cost"],
            random_data["rarity"],
            random_data["attack"],
            random_data["health"]
        )

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        random_data: Dict[str, Any] = random.choice(self.spells)
        if isinstance(name_or_power, str):
            return SpellCard(
                name_or_power,
                random_data["cost"],
                random_data["rarity"],
                random_data["effect_type"]
            )
        elif isinstance(name_or_power, int):
            return SpellCard(
                random_data["name"],
                name_or_power,
                random_data["rarity"],
                random_data["effect_type"]
            )
        return SpellCard(
            random_data["name"],
            random_data["cost"],
            random_data["rarity"],
            random_data["effect_type"]
        )

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        random_data: Dict[str, Any] = random.choice(self.artifacts)
        if isinstance(name_or_power, str):
            return ArtifactCard(
                name_or_power,
                random_data["cost"],
                random_data["rarity"],
                random_data["durability"],
                random_data["effect"]
            )
        elif isinstance(name_or_power, int):
            return ArtifactCard(
                random_data["name"],
                name_or_power,
                random_data["rarity"],
                random_data["durability"],
                random_data["effect"]
            )
        return ArtifactCard(
            random_data["name"],
            random_data["cost"],
            random_data["rarity"],
            random_data["durability"],
            random_data["effect"]
        )

    def create_themed_deck(self, size: int) -> dict:
        themed_deck = Deck()

        for _ in range(size):
            card_type = random.choice(["creature", "spell", "artifact"])
            if card_type == "creature":
                themed_deck.add_card(self.create_creature())
            elif card_type == "spell":
                themed_deck.add_card(self.create_spell())
            elif card_type == "artifact":
                themed_deck.add_card(self.create_artifact())

        return {
            "cards": themed_deck.deck,
            "stats": themed_deck.get_deck_stats()
        }

    def get_supported_types(self) -> dict:
        return {
            "creatures": [card["name"] for card in self.creatures],
            "spells": [card["name"] for card in self.spells],
            "artifacts": [card["name"] for card in self.artifacts]
        }
