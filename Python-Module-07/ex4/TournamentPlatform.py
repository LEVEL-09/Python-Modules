from .TournamentCard import TournamentCard
from typing import Dict


class TournamentPlatform():
    def __init__(self) -> None:
        self.cards: Dict[str, TournamentCard] = {}
        self.match_count = 0

    def register_card(self, card: TournamentCard) -> str:
        self.cards[card.card_id] = card
        return card.card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        c1: TournamentCard = self.cards[card1_id]
        c2: TournamentCard = self.cards[card2_id]

        c1.attack(c2)
        c2.attack(c1)
        c1.defend(c2.value_attack)
        c2.defend(c1.value_attack)
        if c1.value_health > c2.value_health:
            winner = c1
            loser = c2
        else:
            winner = c2
            loser = c1

        winner.rating += 16
        winner.wins += 1
        loser.rating -= 16
        loser.losses += 1
        self.match_count += 1
        return {
            "winner": winner.card_id,
            "loser": loser.card_id,
            "winner_rating": winner.rating,
            "loser_rating": loser.rating
        }

    def get_leaderboard(self) -> list:
        def fun(value) -> int:
            return value.rating

        return sorted(
            self.cards.values(),
            key=fun,
            reverse=True
        )

    def generate_tournament_report(self) -> dict:
        def rating_avg() -> int:
            avg = 0
            for i in self.cards.values():
                avg += i.rating
            return int(avg/len(self.cards))

        return {
            "total_cards": len(self.cards),
            "matches_played": self.match_count,
            "avg_rating": rating_avg()
        }
