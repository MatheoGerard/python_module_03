import sys


def split_elem(argument: str, inventory: dict[str, int]) -> None:
    element_to_add: list[str] = argument.split(":")
    name_elem: str = ""
    try:
        name_elem: str = str(element_to_add[0])
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


if __name__ == "__main__":
    inventory: dict[str, int] = parsing_args(sys.argv)
    print(f"Got inventory: {inventory}")
    items_list: list[str] = list(inventory.keys())
    items_count: list[int] = list(inventory.values())
    print(f"Item list: {items_list}")
    print(f"Total quantity of the {len(items_list)} items: {sum(items_count)}")
