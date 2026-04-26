from ex0.Card import Card


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 effect_type: str) -> None:
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        game_state.update({"effect": self.effect_type})
        return game_state

    def resolve_effect(self, targets: list) -> dict:
        return {
            "targets_list": targets,
            "damage_all": len(targets)*3
        }
