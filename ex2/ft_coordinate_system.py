import math


def fill_tuples(usr_input: list[str], player_pos: list[float]) -> bool:
    if not len(usr_input) == 3:
        print("Invalid syntax")
        return False
    try:
        for i in range(0, len(usr_input)):
            player_pos.append(float(usr_input[i]))
        return True
    except ValueError:
        print("Invalid syntax")
        return False


def get_player_pos() -> None:
    print("Get a first set of coordinates")
    is_good_pos: bool = False
    player_pos: list[float] = []
    while not is_good_pos:
        is_good_pos = True
        user_input: list[str] = input(
            "Enter new coordinates as floats in format 'x,y,z': "
        ).split(",")
        is_good_pos = fill_tuples(user_input, player_pos)
    print(player_pos)


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    get_player_pos()
