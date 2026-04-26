from ex0.main import Rarity
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck


if __name__ == "__main__":
    print("\n=== DataDeck Deck Builder ===")

    print("\nBuilding deck with different card types...")
    try:
        creature_card1 = CreatureCard("Fire Dragon", 2, Rarity.C.value, 7, 9)
        creature_card2 = SpellCard("Lightning Bolt", 3, Rarity.U.value,
                                   "Deal 3 damage to target")
        creature_card3 = ArtifactCard("Mana Crystal", 5, Rarity.L.value, 3,
                                      "Permanent: +1 mana per turn")

        deck1 = Deck()
        deck1.add_card(creature_card1)
        deck1.add_card(creature_card2)
        deck1.add_card(creature_card3)

        deck1.shuffle()
        print(f"Deck stats: {deck1.get_deck_stats()}")

        print("\nDrawing and playing cards:")

        for _ in range(3):
            if len(deck1.deck) == 0:
                print("\nNo card to draw!")
                break

            card = deck1.draw_card()
            deck1.remove_card(card.name)
            print(f"\nDrew: {card.name} ({type(card).__name__})")
            state = {
                "card_played": card.name,
                "mana_used": card.cost,
            }
            print(f"Play result: {card.play(state)}")

        targets_lists = [creature_card1, creature_card3]
        creature_card2.resolve_effect(targets_lists)

        print("\nPolymorphism in action: Same interface, "
              "different card behaviors!")
    except Exception as e:
        print(f"ERROR: {e}")
