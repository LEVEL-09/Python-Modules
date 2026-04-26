from .CardFactory import CardFactory
from .GameStrategy import GameStrategy


class GameEngine():
    def __init__(self):
        self.card_factory = None
        self.strategy = None
        self.turn_count = 0

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self.card_factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> dict:
        self.turn_count += 1
        hand = self.card_factory.create_themed_deck(3)["cards"]
        battlefield = ["Friendly Creature", "Friendly Artifact"]
        return self.strategy.execute_turn(hand, battlefield)

    def get_engine_status(self) -> dict:
        return {
            "turns_simulated": self.turn_count,
            "strategy_used": self.strategy.get_strategy_name(),
            "total_damage": self.simulate_turn().get("damage_dealt", 0),
            "cards_created":
            len(self.card_factory.create_themed_deck(3)['cards'])
        }
