if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")

    alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    bob = {'first_kill', 'level_10', 'boss_slayer', 'collector', 'first_kill'}
    charlie = {'level_10', 'treasure_hunter', 'boss_slayer',
               'speed_demon', 'perfectionist'}

    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")

    print("\n=== Achievement Analytics ===")

    unique_achievements = alice.union(bob, charlie)
    print(f"All unique achievements: {unique_achievements}")
    print(f"All unique achievements: {len(unique_achievements)}\n")

    common_to_all = alice.intersection(bob, charlie)
    print(f"Common to all players: {common_to_all}")

    players = [alice, bob, charlie]
    rare_achievements = set()
    for achievement in unique_achievements:
        cont = 0
        for i in players:
            if achievement in i:
                cont += 1
        if cont == 1:
            rare_achievements.add(achievement)
    print(f"Rare achievements (1 player): {rare_achievements}\n")

    print(f"Alice vs Bob common: {alice.intersection(bob)}")
    print(f"Alice unique: {alice.difference(bob)}")
    print(f"Bob unique: {bob.difference(alice)}")
