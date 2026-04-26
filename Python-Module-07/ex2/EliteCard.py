from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str, value_attack: int,
                 value_health: int, damage_block: int,
                 combat_type: str, mana: int,
                 magic_level: int):
        if value_attack < 0:
            raise ValueError("Attack must be 0 or more")
        if value_health < 0:
            raise ValueError("Health must be 0 or more")
        if damage_block < 0:
            raise ValueError("Damage block must be more then 0")
        if mana < 0:
            raise ValueError("mana must be 0 or more")
        if magic_level < 0:
            raise ValueError("Magic level must be 0 or more")
        self.value_attack = value_attack
        self.value_health = value_health
        self.damage_block = damage_block
        self.combat_type = combat_type
        self.mana = mana
        self.magic_level = magic_level
        super().__init__(name, cost, rarity)

    def play(self, game_state: dict) -> dict:
        return game_state

    def attack(self, target) -> dict:
        return {
            "attacker": self.name,
            "target": target.name,
            "damage": self.value_attack,
            "combat_type": self.combat_type
        }

    def defend(self, incoming_damage: int) -> dict:
        self.value_health -= incoming_damage
        return {
            "defender": self.name,
            "damage_taken": max(0, incoming_damage - self.damage_block),
            "damage_blocked": self.damage_block,
            "still_alive": self.value_health > 0
        }

    def get_combat_stats(self) -> dict:
        return {
            "damage": self.value_attack,
            "combat": self.combat_type
        }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": [target.name for target in targets],
            "mana_used": 4
        }

    def channel_mana(self, amount: int) -> dict:
        return {
            "channeled": amount,
            "total_mana": self.mana
        }

    def get_magic_stats(self) -> dict:
        return {
            "magic": self.mana,
            "level": self.magic_level
        }
