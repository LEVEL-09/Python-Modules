from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.GameEngine import GameEngine

if __name__ == "__main__":
    print("\n=== DataDeck Game Engine ===")

    print("\nConfiguring Fantasy Card Game...")

    try:
        card_factory = FantasyCardFactory()
        strategy = AggressiveStrategy()
        game_engine = GameEngine()
        game_engine.configure_engine(card_factory, strategy)

        print(f'Factory: {card_factory.__class__.__name__}')
        print(f'Strategy: {strategy.__class__.__name__}')
        print(f"Available types: "
              f"{game_engine.card_factory.get_supported_types()}")

        print("\nSimulating aggressive turn...")
        deck = game_engine.card_factory.create_themed_deck(3)['cards']
        print(
            f"Hand: {[f'{card.name} ({card.cost})' for card in deck]}"
        )

        print("\nTurn execution:")
        print(f"Strategy: {strategy.get_strategy_name()}")
        print(f"Actions: {game_engine.simulate_turn()}")

        print("\nGame Report:")
        print(game_engine.get_engine_status())

        print("\nAbstract Factory + Strategy Pattern: "
              "Maximum flexibility achieved")
    except Exception as e:
        print(f"Error during game simulation: {e}")
