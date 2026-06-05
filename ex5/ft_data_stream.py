import random
import typing


def gen_event():
    actions_list: list[str] = [
        "swim",
        "eat",
        "run",
        "grab",
        "move",
        "climb",
        "sleep",
        "release",
        "use",
    ]
    name_list: list[str] = [
        "dylan",
        "alice",
        "bob",
        "charlie",
    ]
    name: str = name_list[random.randrange(0, len(name_list))]
    action: str = actions_list[random.randrange(0, len(actions_list))]
    return_tuple: tuple[str, str] = (name, action)
    yield return_tuple


def consume_event(events: list[tuple[str, str]]):
    yield events.pop(random.randrange(0, len(events)))


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    for i in range(0, 1000):
        name_action: tuple[str, str] = next(gen_event())
        print(f"Event {i}: Player {name_action[0]} did action {name_action[1]}")
    ten_tuples: list[tuple[str, str]] = []
    for _ in range(0, 10):
        ten_tuples.append(next(gen_event()))
    print(f"Built list of 10 events: {ten_tuples}")
    for _ in range(0, len(ten_tuples)):
        print(f"Got event from list: {next(consume_event(ten_tuples))}")
        print(f"Remains in list: {ten_tuples}")
