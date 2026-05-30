import math


def distance_function(
    p1: tuple[float, float, float], p2: tuple[float, float, float]
) -> float:
    distance: float = math.sqrt(
        (p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2 + (p2[2] - p1[2]) ** 2
    )
    return distance


def fill_tuples(usr_input: list[str], player_pos: list[float]) -> bool:
    if not len(usr_input) == 3:
        if len(usr_input) < 3:
            print("Not enough arguments")
        else:
            print("Too many arguments")
        return False
    i: int = 0
    try:
        while i < len(usr_input):
            player_pos.append(float(usr_input[i]))
            i += 1
        return True
    except ValueError:
        player_pos.clear()
        print(
            f"\033[31mError on parameter '{usr_input[i]}': could not convert string to float: '{usr_input[i]}'\033[0m"
        )
        return False


def get_player_pos() -> tuple[float, float, float]:
    is_good_pos: bool = False
    player_pos: list[float] = []
    while not is_good_pos:
        is_good_pos = True
        user_input: list[str] = input(
            "Enter new coordinates as floats in format 'x,y,z': "
        ).split(",")
        is_good_pos = fill_tuples(user_input, player_pos)
    position: tuple[float, float, float] = (player_pos[0], player_pos[1], player_pos[2])
    return position


def main() -> None:
    print("=== Game Coordinate System ===")
    print("Get a first set of coordinates")
    first_position: tuple[float, float, float] = get_player_pos()
    print(f"Got a first tuple: {first_position}")
    print(
        f"It includes: X={first_position[0]}, Y={first_position[1]}, Z={first_position[2]}"
    )
    center: tuple[float, float, float] = (0.0, 0.0, 0.0)
    print(f"Distance to center: {distance_function(center, first_position)}")
    print()
    print("Get a second set of coordinates")
    second_position: tuple[float, float, float] = get_player_pos()
    print(
        f"Distance between the 2 sets of coordinates: {distance_function(first_position, second_position)}"
    )


if __name__ == "__main__":
    main()
