import random


class Player:
    def __init__(self, name: str, achivements: set[str]) -> None:
        self.set_achivements(achivements)
        self.set_name(name)

    def set_name(self, name) -> None:
        self._name = name

    def get_name(self) -> str:
        return self._name

    def set_achivements(self, achivements) -> None:
        self._achivements = achivements

    def get_achivements(self) -> set[str]:
        return self._achivements

    def get_achivements_nb(self) -> int:
        return len(self._achivements)

    def show(self):
        print(f"Player {self.get_name()}: {self.get_achivements()}")

    @classmethod
    def generate_player(cls, name, achivements) -> "Player":
        return cls(name, achivements)


def gen_player_achievements() -> set[str]:
    achivement_list: list[str] = [
        "Crafting Genius",
        "Strategist",
        "World Savior",
        "Speed Runner",
        "Survivor",
        "Master Explorer",
        "Treasure Hunter",
        "Unstoppable",
        "First Steps",
        "Collector Supreme",
        "Untouchable",
        "Sharp Mind",
        "Boss Slayer",
    ]
    achivement: set[str] = set()
    nb_achivements = random.randrange(0, len(achivement_list))
    i: int = 0
    while i < nb_achivements:
        achivement.add(achivement_list[random.randrange(0, len(achivement_list))])
        i += 1
    return achivement


def main_player():
    player_name_list: list[str] = [
        "Alice",
        "Martin",
        "Imane",
        "Matheo",
        "Jhon",
        "Mike",
        "Alex",
        "Lucette",
        "Simon",
        "Lucas",
        "Julie",
    ]
    players: list[Player] = []
    name_take: list[int] = []
    nb_players: int = random.randrange(4, len(player_name_list))
    i: int = 0
    while i < nb_players:
        name_index: int = random.randrange(0, len(player_name_list))
        while name_index in name_take:
            name_index: int = random.randrange(0, len(player_name_list))
        name_take.append(name_index)
        player_name: str = player_name_list[name_index]
        players.append(Player.generate_player(player_name, gen_player_achievements()))
        i += 1
    for player in players:
        player.show()
    print()
    sets_players: list[set[str]] = [p.get_achivements() for p in players]
    all_achivements: set[str] = set.union(*sets_players)
    print(f"All distinct achievements: {all_achivements}")
    print()
    shared: set[str] = set.intersection(*sets_players)
    print(f"Common achievements: {shared}")
    print()
    i = 0
    while i < len(players):
        set_without_actual: list[set[str]] = sets_players[:i] + sets_players[i + 1 :]
        unique: set[str] = sets_players[i].difference(*set_without_actual)
        print(f"Only {players[i].get_name()} has: {unique}")
        i += 1


if __name__ == "__main__":
    main_player()
