import math


def casting_input(str_input: str) -> None:
    try:




def get_player_pos() -> None:
    print("Get a first set of coordinates")
    is_good_pos = False
    while not is_good_pos:
        user_input: list[str] = input(
            "Enter new coordinates as floats in format 'x,y,z': "
        ).split()
        for _ in user_input:
            try:



if __name__ == "__main__":
    print("=== Game Coordinate System ===")
