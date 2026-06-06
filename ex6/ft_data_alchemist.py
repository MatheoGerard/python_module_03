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
    all_scored: dict[str, int] = {
        name: random.randrange(0, 1000) for name in all_name_capitalize
    }
    print(f"Score dict: {all_scored}")
    average: float = round(
        sum(all_scored.values()) / len(all_name_capitalize), 2
    )
    print(f"Score average is {average}")
    high_score: dict[str, int] = {
        name: all_scored[name]
        for name in all_scored
        if all_scored[name] > average
    }
    print(f"High scores: {high_score}")
