from ex0.main import Rarity
from .TournamentCard import TournamentCard
from .TournamentPlatform import TournamentPlatform

if __name__ == "__main__":
    print("\n=== DataDeck Tournament Platform ===")

    try:
        print("\nRegistering Tournament Cards...")
        platform = TournamentPlatform()

        card1 = TournamentCard("Fire Dragon", "dragon_001",
                               5, Rarity.C.value, 1, 30)
        print(f"{card1.name} (ID: {platform.register_card(card1)}):")
        print(f"- Interfaces: {card1.get_tournament_stats()['Interfaces']}")
        print(f"- Rating: {card1.get_tournament_stats()['Rating']}")
        print(f"- Record: {card1.get_tournament_stats()['Record']}")

        card2 = TournamentCard("Ice Wizard", "wizard_001", 6, Rarity.C.value,
                               24, 9)
        print(f"\n{card2.name} (ID: {platform.register_card(card2)}):")
        print(f"- Interfaces: {card2.get_tournament_stats()['Interfaces']}")
        print(f"- Rating: {card2.get_tournament_stats()['Rating']}")
        print(f"- Record: {card2.get_tournament_stats()['Record']}")

        match = platform.create_match(card1.card_id, card2.card_id)
        print("\nCreating tournament match...")
        print(f"Match result: {match}")

        print("\nTournament Leaderboard:")
        i = 1
        for card in platform.get_leaderboard():
            print(f"{i}. {card.name} - Rating: {card.rating} "
                  f"({card.get_tournament_stats()['Record']})")
            i += 1

        print("\nPlatform Report:")
        print(platform.generate_tournament_report())

        print("\n=== Tournament Platform Successfully Deployed! ===")
        print("All abstract patterns working together harmoniously!")
    except Exception as e:
        print(f"Error: {e}")
