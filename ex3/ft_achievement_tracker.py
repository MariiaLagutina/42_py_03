#!/usr/bin/env python3

def achievement_tracker() -> None:
    """ Function to track and display player achievements. """

    print("=== Achievement Tracker System ===")
    print()
    players = {
        "Mary": [
            "first_kill",
            "level_10",
            "treasure_hunter",
            "speed_demon",
            "hardcore_mode",
            "first_kill",
            "double_kill"
        ],
        "Hans": [
            "first_kill",
            "level_10",
            "double_kill",
            "boss_slayer",
            "collector",
            "double_kill",
            "multi_kill",
            "sniper_master"
        ],
        "Anna": [
            "level_10",
            "treasure_hunter",
            "boss_slayer",
            "speed_demon",
            "perfectionist",
            "sniper_master"
        ],
        "Nick": [
            "level_10",
            "treasure_hunter",
            "boss_slayer",
            "speed_demon",
            "perfectionist",
            "hardcore_mode"
        ]
    }
    players = {name: set(ach) for name, ach in players.items()}

    for name, achievements in players.items():
        print(f"Player {name} achievements: {achievements}")

    print("\n=== Achievement Analytics ===")

    all_achievements = set().union(*players.values())
    print(f"All unique achievements: {all_achievements}")
    print(f"Total unique achievements: {len(all_achievements)}")
    print()

    common_to_all = set.intersection(*players.values())
    print(f"Common to all players: {common_to_all}")

    all_counts = []
    for ach_set in players.values():
        all_counts.extend(list(ach_set))

    rare_achievements = {ach for ach in all_achievements
                         if all_counts.count(ach) == 1}
    print(f"Rare achievements (1 player): {rare_achievements}")
    print()

    mary_hans_common = players["Mary"].intersection(players["Hans"])
    mary_only = players["Mary"].difference(players["Hans"])
    hans_only = players["Hans"].difference(players["Mary"])

    print(f"Mary vs Hans common: {mary_hans_common}")
    print(f"Mary unique: {mary_only}")
    print(f"Hans unique: {hans_only}")


if __name__ == "__main__":
    achievement_tracker()
