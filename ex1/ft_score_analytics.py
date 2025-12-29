#!/usr/bin/env python3

import sys


def ft_score_analytics() -> None:
    """ Function to analyze and display score-related command
    line arguments. """

    print("=== Player Score Analytics ===")
    if len(sys.argv) == 1:
        print(f"No scores provided. Usage: {sys.argv[0]} "
              f"<score1> <score2> ...")
        return

    scores = []

    for arg in sys.argv[1:]:
        try:
            score = int(arg)
            scores.append(score)
        except ValueError:
            print(f"Warning: '{arg}' is not a valid score and will "
                  f"be ignored.")
    if scores:
        total_score = sum(scores)
        average_score = total_score / len(scores)
        max_score = max(scores)
        min_score = min(scores)

        print(f"Scores processed: {scores}")
        print(f"Total players: {len(scores)}")
        print(f"Total Score: {total_score}")
        print(f"Average Score: {average_score}")
        print(f"High score: {max_score}")
        print(f"Low score: {min_score}")
        print(f"Score range: {max_score - min_score}")
    else:
        print("Error: No valid numerical scores found in the input.")
        return


if __name__ == "__main__":
    ft_score_analytics()
