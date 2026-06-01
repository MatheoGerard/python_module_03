import sys


def split_elem(argument: str, inventory: dict[str, int]) -> None:
    element_to_add: list[str] = argument.split(":")
    name_elem: str = ""
    try:
        name_elem = str(element_to_add[0])
        if name_elem in inventory.keys():
            print(f"Redundant item '{name_elem}' - discarding")
            return
        nb_elem: int = int(element_to_add[1])
        inventory.update({name_elem: nb_elem})
    except ValueError as e:
        print(f"Quantity error for '{name_elem}': {e}")


def parsing_args(args_list: list[str]) -> dict[str, int]:
    inventory: dict[str, int] = dict()
    for args in args_list[1:]:
        if ":" not in args:
            print(f"Error - invalid parameter '{args}'")
            continue
        split_elem(args, inventory)
    return inventory


def calcul_pourcentage(item_nb: int, items_count: int) -> float:
    pourcentage: float = item_nb / items_count * 100
    return round(pourcentage, 1)


def find_max(inventory: dict[str, int], items_list: list[str]) -> tuple[str, int]:
    high: int = inventory[items_list[0]]
    name_high: str = items_list[0]
    for item in items_list[1:]:
        if inventory[item] > high:
            high = inventory[item]
            name_high = item
    return_set: tuple[str, int] = (name_high, high)
    return return_set


def find_min(inventory: dict[str, int], items_list: list[str]) -> tuple[str, int]:
    low: int = inventory[items_list[0]]
    name_low: str = items_list[0]
    for item in items_list[1:]:
        if inventory[item] < low:
            low = inventory[item]
            name_low = item
    return_set: tuple[str, int] = (name_low, low)
    return return_set


if __name__ == "__main__":
    inventory: dict[str, int] = parsing_args(sys.argv)
    print(f"Got inventory: {inventory}")
    items_list: list[str] = list(inventory.keys())
    items_count: list[int] = list(inventory.values())
    print(f"Item list: {items_list}")
    print(f"Total quantity of the {len(items_list)} items: {sum(items_count)}")
    for item in inventory.keys():
        print(
            f"Item {item} represents {calcul_pourcentage(inventory[item], sum(items_count))}%"
        )
    if len(sys.argv) > 1:
        max_set: tuple[str, int] = find_max(inventory, items_list)
        print(f"Item most abundant: {max_set[0]} with quantity {max_set[1]}")
        min_set: tuple[str, int] = find_min(inventory, items_list)
        print(f"Item least abundant: {min_set[0]} with quantity {min_set[1]}")
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")
