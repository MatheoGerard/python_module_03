import random


if __name__ == "__main__":
    print("=== Game Data Alchemist ===")
    print()
    name_list: list[str] = [
        "Alice",
        "bob",
        "Charlie",
        "dylan",
        "Emma",
        "Gregory",
        "john",
        "kevin",
        "Liam",
    ]
    print(f"Initial list of players: {name_list}")
    all_name_capitalize: list[str] = [name.capitalize() for name in name_list]
    print(f"New list with all names capitalized: {all_name_capitalize}")
    only_capitalize: list[str] = [
        name for name in name_list if name == name.capitalize()
    ]
    print(f"New list of capitalized names only: {only_capitalize}")
    print()
    # TODO: mettre le dictionnaire en full capitalized avec un score random.randrange..
    all_scored: dict[str, int] = {}
