#!/usr/bin/env python3

import sys
import math


def distance(p: tuple) -> float:
    """Calculates the Euclidean distance from the origin to point p."""
    return math.sqrt(sum(coord**2 for coord in p))


def ft_coordinate_system() -> None:
    """Processes 3D coordinates from command line and
    demonstrates tuple power."""
    print("=== Game Coordinate System ===")

    # pos = (10, 20, 5)
    # print(f"Position created: {pos}")
    # print(f"Distance between (0, 0, 0) and {pos}: {distance(pos):.2f}")

    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} \"x,y,z\"")
        return

    coord_str = sys.argv[1]
    print(f"Parsing coordinates: \"{coord_str}\"")

    parts = coord_str.split(',')
    if len(parts) != 3:
        print("Error: Expected coordinates in format x,y,z")
        return

    try:
        position = tuple(int(p) for p in parts)
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")
        return

    print(f"Position created: {position}")

    print(f"Distance between (0, 0, 0) and {position}:"
          f"{distance(position):.2f}")

    print("\nUnpacking demonstration:")
    x, y, z = position
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    ft_coordinate_system()
