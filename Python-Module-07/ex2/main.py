from ex2.EliteCard import EliteCard
from ex0.main import Rarity
from typing import List


if __name__ == "__main__":
    print("\n=== DataDeck Ability System ===\n")
    try:
        elite_card1 = EliteCard("Arcane Warrior", 35, Rarity.L.value, 5,
                                100, 3, "melee", 7, 9)
        elite_card2 = EliteCard("Enemy", 20, Rarity.L.value, 5, 40, 99,
                                "dance", 67, 10)

        print("EliteCard capabilities:")
        print("- Card: ['play', 'get_card_info', 'is_playable']")
        print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
        print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")

        print(f"\nPlaying {elite_card1.name} (Elite Card):\n")

        print("Combat phase:")
        print(f"Attack result: {elite_card1.attack(elite_card2)}")
        print(f"Defense result: "
              f"{elite_card1.defend(elite_card2.value_attack)}")

        print("\nMagic phase:")
        elite_card3 = EliteCard("Enemy1", 49, Rarity.L.value, 0,
                                88, 10, "melee", 79, 1)
        elite_card4 = EliteCard("Enemy2", 14, Rarity.L.value, 36,
                                97, 25, "melee", 45, 50)
        enemy_list: List[EliteCard] = [elite_card3, elite_card4]

        print(f"Spell cast: {elite_card1.cast_spell('Fireball', enemy_list)}")
        print(f"Mana channel: {elite_card1.channel_mana(3)}")

        print("\nMultiple interface implementation successful!")
    except Exception as e:
        print(f"ERROR: {e}")
