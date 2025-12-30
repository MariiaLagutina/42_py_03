#!/usr/bin/env python3

def ft_analytics_dashboard() -> None:
    """Simulated analytics dashboard for an Emerald City game."""
    heroes = [
        {
            "name": "Dorothy",
            "score": 2500,
            "region": "Kansas",
            "achievements": [
                "silver_shoes_bearer",
                "wicked_witch_banisher",
                "pathfinder_of_yellow_brick",
                "Toto_companion",
            ],
        },
        {
            "name": "Scarecrow",
            "score": 1800,
            "region": "Great Cornfield",
            "achievements": [
                "mind_awakened",
                "emerald_scholar",
                "strategist_of_oz",
            ],
        },
        {
            "name": "Tin Man",
            "score": 2100,
            "region": "Winkie Country",
            "achievements": [
                "heart_of_steel",
                "forest_guardian",
                "compassion_forged",
            ],
        },
        {
            "name": "Lion",
            "score": 2200,
            "region": "Quadling Country",
            "achievements": [
                "courage_unleashed",
                "beast_king_crowned",
                "protector_of_weak",
            ],
        },
        {
            "name": "Glinda",
            "score": 3000,
            "region": "North Oz",
            "achievements": [
                "good_witch_supreme",
                "arcane_protector",
                "keeper_of_balance",
                "light_of_oz",
            ],
        },
    ]

    print("=== Emerald City Analytics Dashboard ===")
    print()
    print("=== List Comprehension Examples ===")

    leaderboard = 2000
    high_scorers = [h["name"] for h in heroes if h["score"] > leaderboard]
    print(f"High scorers (>{leaderboard}): {high_scorers}")

    scores_doubled = [h["score"] * 2 for h in heroes]
    print(f"Scores doubled: {scores_doubled}")

    active_players = [h["name"] for h in heroes if len(h["achievements"]) >= 2]
    print(f"Active players: {active_players}")
    print()

    print("=== Dict Comprehension Examples ===")

    player_scores = {h["name"]: h["score"] for h in heroes}
    print(f"Player scores: {player_scores}")

    high_scorers = 2500
    low_scores = 2000
    score_categories = {
        "high": len([h for h in heroes if h["score"] >= high_scorers]),
        "medium": len([h for h in heroes if low_scores <=
                       h["score"] < high_scorers]),
        "low": len([h for h in heroes if h["score"] < low_scores]),
    }
    print(f"Score categories: {score_categories}")

    achievement_counts = {
        h["name"]: len(h["achievements"]) for h in heroes
    }
    print(f"Achievement counts: {achievement_counts}")
    print()

    print("=== Set Comprehension Examples ===")

    unique_players = {h["name"] for h in heroes}
    print(f"Unique players: {unique_players}")

    unique_achievements = {
        ach for h in heroes for ach in h["achievements"]
    }
    print(f"Unique achievements: {unique_achievements}")

    active_regions = {h["region"] for h in heroes}
    print(f"Active regions: {active_regions}")
    print()

    print("=== Combined Analysis ===")

    total_players = len(heroes)
    total_unique_achievements = len(unique_achievements)
    average_score = sum(h["score"] for h in heroes) / total_players
    top_hero = max(heroes, key=lambda h: h["score"])

    print(f"Total players: {total_players}")
    print(f"Total unique achievements: {total_unique_achievements}")
    print(f"Average score: {average_score:.1f}")
    print(
        f"Top performer: {top_hero['name']} "
        f"({top_hero['score']} points, "
        f"{len(top_hero['achievements'])} achievements)"
    )


if __name__ == "__main__":
    ft_analytics_dashboard()
