from .GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        played = [card.name for card in hand]
        return {
            "cards_played": played,
            "mana_used": 5,
            "targets_attacked": ["Enemy Player"],
            "damage_dealt": 8,
            "battlefield_state": battlefield
        }

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        def priority(target) -> bool:
            return target == "Enemy Player"
        return [sorted(available_targets, key=priority, reverse=True)]
