from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from typing import List
import random


class Deck():
    def __init__(self) -> None:
        self.deck: List[Card] = []

    def add_card(self, card: Card) -> None:
        self.deck.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.deck:
            if card_name == card.name:
                self.deck.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.deck)

    def draw_card(self) -> Card:
        return self.deck[-1]

    def get_deck_stats(self) -> dict:
        return {
            "total_cards": len(self.deck),
            "creatures": len([card for card in self.deck
                              if isinstance(card, CreatureCard)]),
            "spells": len([card for card in self.deck
                           if isinstance(card, SpellCard)]),
            "artifacts": len([card for card in self.deck
                              if isinstance(card, ArtifactCard)]),
            "avg_cost": round(sum([i.cost for i
                                   in self.deck]) / len(self.deck), 2)
        }
