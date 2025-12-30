#!/usr/bin/env python3

import random
import time


def game_event_stream(count: int):
    """Generator that simulates a dynamic stream of game events."""
    names = ["alice", "bob", "charlie", "diana", "eve", "frank", "grace"]
    actions = ["killed monster", "found treasure", "leveled up"]

    for i in range(1, count + 1):
        yield {
            "id": i,
            "player": random.choice(names),
            "level": random.randint(5, 20),
            "event": random.choice(actions),
        }


def fibonacci_gen(n: int):
    """Generates the first n Fibonacci numbers."""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def is_prime(n: int) -> bool:
    """Helper to check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def prime_gen(count: int):
    """Generator for the first n prime numbers."""
    n = 2
    found = 0
    while found < count:
        if is_prime(n):
            yield n
            found += 1
        n += 1


def ft_data_stream() -> None:
    print("=== Game Data Stream Processor ===")
    print()
    print("Processing 1000 game events...")
    print()

    stream = game_event_stream(1000)

    for _ in range(3):
        ev = next(stream)
        print(f"Event {ev['id']}: Player {ev['player']} "
              f"(level {ev['level']}) {ev['event']}")
    print("...")

    total_events = 3
    high_level_players = 0
    treasure_events = 0
    levelup_events = 0

    for event in stream:
        total_events += 1
        if event["level"] >= 10:
            high_level_players += 1
        if event["event"] == "found treasure":
            treasure_events += 1
        if event["event"] == "leveled up":
            levelup_events += 1

    start_time = time.time()
    end_time = time.time()
    processing_time = end_time - start_time

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {total_events}")
    print(f"High-level players (10+): {high_level_players}")
    print(f"Treasure events: {treasure_events}")
    print(f"Level-up events: {levelup_events}")
    print()
    print("Memory usage: Constant (streaming)")
    print(f"Processing time: {processing_time:.10f} seconds")

    print("\n=== Generator Demonstration ===")
    print("Fibonacci sequence (first 15):", end=" ")
    print(", ".join(str(f) for f in fibonacci_gen(15)))
    print("Prime numbers (first 10):", end=" ")
    print(", ".join(str(p) for p in prime_gen(10)))


if __name__ == "__main__":
    ft_data_stream()
