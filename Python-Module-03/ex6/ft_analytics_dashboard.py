if __name__ == "__main__":
    print("=== Game Analytics Dashboard ===\n")

    player = [
        {"name": "alice", "score": 2300,
         "achievements": ["first_kill", "level_10"],
         "active": True, "regions": "center"},

        {"name": "diana", "score": 2800,
         "achievements": ["hacker"],
         "active": False, "regions": "east"},

        {"name": "bob", "score": 300,
         "achievements": ["love flower", "kill women", "eat human"],
         "active": True, "regions": "north"},

        {"name": "charlie", "score": 2150,
         "achievements": ["level_100", "found dragon egg", "first_kill"],
         "active": True, "regions": "east"}
    ]

    print("=== List Comprehension Examples ===")
    height_score = [p["name"] for p in player if p["score"] > 2000]
    print(F"High scorers (>2000): {height_score}")

    score_doubled = [2 * s["score"] for s in player]
    print(F"Scores doubled: {score_doubled}")

    active_players = [p["name"] for p in player if p["active"]]
    print(F"Active players: {active_players}")

    print("\n=== Dict Comprehension Examples ===")
    player_score = {p["name"]: p["score"] for p in player}
    print(F"Player scores: {player_score}")

    score_categories = {
        "high": len([p for p in player if p["score"] > 2500]),
        "medium": len([p for p in player if 500 <= p["score"] <= 2500]),
        "low": len([p for p in player if p["score"] < 500])
    }
    print(F"Score categories: {score_categories}")

    achievement_counts = {p["name"]: len(i["achievements"]) for i in player
                          for p in player}
    print(f"Achievement counts: {achievement_counts}")

    print("\n=== Set Comprehension Examples ===")
    unique_players = {p["name"] for p in player}
    print(f"Unique players: {unique_players}")

    unique_achievement = {unique for p in player
                          for unique in p["achievements"]}
    print(f"Unique achievements: {unique_achievement}")

    active_regions = {p["regions"] for p in player}
    print(F"Unique achievements: {active_regions}")

    print("\n=== Combined Analysis ===")
    total_players = len([p['name'] for p in player])
    print(f"Total players: {total_players}")

    total_unique_achievement = len({unique for p in player
                                    for unique in p['achievements']})
    print(f"Total unique achievements: {total_unique_achievement}")

    average_score = sum([p["score"] for p in player])
    print(F"Average score: {average_score / total_players}")

    max_score = max([p["score"] for p in player])
    for p in player:
        for key in p:
            if p[key] == max_score:
                top_performer_achievements = len(p["achievements"])
                top_performer = p
                break

    print(f"Top performer: {top_performer['name']} "
          f"({top_performer['score']} points, {top_performer_achievements} "
          "achievements)")
