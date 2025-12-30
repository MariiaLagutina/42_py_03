#!/usr/bin/env python3

def ft_inventory_system() -> None:
    """Player Inventory System with Analytics."""
    print("=== Player Inventory System ===")
    print()

    inventory = {
        "sword": {
            "name": "Excalibur",
            "category": "weapon",
            "rarity": "rare",
            "quantity": 1,
            "value": 500,
        },
        "axe": {
            "name": "Gnome Axe",
            "category": "weapon",
            "rarity": "uncommon",
            "quantity": 2,
            "value": 200,
        },
        "potion": {
            "name": "Health Potion",
            "category": "consumable",
            "rarity": "common",
            "quantity": 5,
            "value": 10,
        },
        "shield": {
            "name": "Dragon Shield",
            "category": "armor",
            "rarity": "epic",
            "quantity": 1,
            "value": 300,
        },
        "arrow": {
            "name": "Arrow",
            "category": "ammo",
            "rarity": "common",
            "quantity": 20,
            "value": 5,
        },
        "bow": {
            "name": "Legalass Bow",
            "category": "weapon",
            "rarity": "uncommon",
            "quantity": 1,
            "value": 150,
        }
    }

    players = {
        "Alice": {
            "username": "LegendHero",
            "level": 10,
            "inventory": {
                "sword": 1,
                "potion": 11,
                "shield": 1,
                "bow": 1,
                "arrow": 20,
            },
        },
        "Bobby": {
            "username": "SniperKing",
            "level": 8,
            "inventory": {
                "bow": 1,
                "arrow": 20,
                "potion": 5,
                "shield": 1,
            },
        },
        "Henri": {
            "username": "KingSlayer",
            "level": 12,
            "inventory": {
                "axe": 1,
                "shield": 1,
                "potion": 10,
            },
        },
    }

    def print_player_report(p_name: str):
        """Prints a report of a player's inventory."""
        p_data = players[p_name]
        print(f"=== {p_name}'s Inventory ===")

        total_gold = 0
        total_items = 0
        cat_counts = {}

        for item_id, quantity in p_data["inventory"].items():
            item_info = inventory.get(item_id)
            if item_info:
                item_total = quantity * item_info["value"]
                total_gold += item_total
                total_items += quantity

                cat = item_info["category"]
                cat_counts[cat] = cat_counts.get(cat, 0) + 1

                print(f"{item_info['name']} ({item_info['category']},"
                      f" {item_info['rarity']}): {quantity} x "
                      f"{item_info['value']} gold each = {item_total} gold")

        print(f"Inventory value: {total_gold} gold")
        print(f"Item count: {total_items} items")
        print(f"Categories: {cat_counts}")
        return total_gold, total_items

    print_player_report("Alice")

    item_id = "potion"
    amount = 2
    print(f"\n=== Transaction: Alice gives Bobby {amount} {item_id}s ==")
    alice_inv = players["Alice"]["inventory"]
    bobby_inv = players["Bobby"]["inventory"]

    if alice_inv.get(item_id, 0) >= amount:
        alice_inv.update({item_id: alice_inv[item_id] - amount})
        bobby_inv.update({item_id: bobby_inv.get(item_id, 0) + amount})
        print("Transaction successful!")
        print()
        print("=== Updated Inventories ===")
        print(f"Alice potions: {players['Alice']['inventory']['potion']}")
        print(f"Bobby potions: {players['Bobby']['inventory']['potion']}")
    else:
        print("Transaction failed: Not enough items.")

    def calculate_total_gold(player_inventory: dict) -> int:
        """Calculates total gold value of a player's inventory."""
        total = 0
        for item_id, quantity in player_inventory.items():
            item_info = inventory.get(item_id)
            if item_info:
                total += quantity * item_info["value"]
        return total

    def calculate_total_items(player_inventory: dict) -> int:
        """Calculates total number of items in a player's inventory."""
        total = 0
        for quantity in player_inventory.values():
            total += quantity
        return total

    richest_player = None
    richest_gold = 0

    for name, data in players.items():
        gold = calculate_total_gold(data["inventory"])
        if gold > richest_gold:
            richest_gold = gold
            richest_player = name

    most_items_player = None
    most_items = 0

    for name, data in players.items():
        items = calculate_total_items(data["inventory"])
        if items > most_items:
            most_items = items
            most_items_player = name

    item_owners = {}

    for data in players.values():
        for item_id in data["inventory"]:
            item_owners[item_id] = item_owners.get(item_id, 0) + 1

    rarest_items = []
    for item_id, count in item_owners.items():
        if count == 1:
            rarest_items.append(item_id)
    rarest_item_names = [inventory[item]["name"] for item in rarest_items]

    print("\n=== Inventory Analytics ===")
    print(f"Most valuable player: {richest_player} ({richest_gold} gold)")
    print(f"Most items: {most_items_player} ({most_items} items)")
    print(f"Rarest items: {', '.join(rarest_item_names)}")


if __name__ == "__main__":
    ft_inventory_system()
