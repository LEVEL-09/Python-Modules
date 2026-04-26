from ex0.CreatureCard import CreatureCard
from enum import Enum


class Rarity(Enum):
    L = "Legendary"
    R = "Rare"
    C = "common"
    U = "Uncommon"


if __name__ == "__main__":
    print("\n=== DataDeck Card Foundation ===")

    print("\nTesting Abstract Base Class Design:\n")

    try:
        card_1 = CreatureCard("Fire Dragon", 5, Rarity.L.value, 7, 5)
        card_2 = CreatureCard("Goblin Warrior", 1, Rarity.U.value, 1, 3)
        available_mana = 6

        print("CreatureCard Info:")
        print(card_1.get_card_info())

        print("\nPlaying Fire Dragon with 6 mana available:")
        print(f"Playable: {card_1.is_playable(available_mana)}")

        state = {
            "card_played": card_1.name,
            "mana_used": card_1.cost,
        }
        print(f"Play result: {card_1.play(state)}")

        print("\nFire Dragon attacks Goblin Warrior:")
        print(f"Attack result: {card_1.attack_target(card_2)}")

        print("\nTesting insufficient mana (3 available):")
        available_mana = 3
        print(f"Playable: {card_1.is_playable(available_mana)}")

        print("\nAbstract pattern successfully demonstrated!")
    except Exception as e:
        print(f"ERROR: {e}")
