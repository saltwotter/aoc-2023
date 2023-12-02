import re
from math import prod


def process_lines(string):
    game_str, all_plays_str = string.split(": ")
    game_num = int(re.search("\d+", game_str, flags=re.IGNORECASE).group())
    all_games = [
        {b: int(a) for a, b in [y.split(" ") for y in x.split(", ")]}
        for x in all_plays_str.split("; ")
    ]
    return game_num, all_games


def game_valid(game: list[dict[str, int]], actual: dict[str, int]) -> bool:
    for hand in game:
        for color, val in hand.items():
            if val > actual[color]:
                return False
    return True


def get_min_quantities(game: list[dict[str, int]]) -> dict[str, int]:
    bag = {"red": 0, "green": 0, "blue": 0}
    for hand in game:
        for color, val in hand.items():
            bag[color] = val if bag[color] < val else bag[color]
    return bag


def get_power_of_quantities(bag: dict[str, int]) -> int:
    return prod(bag.values())


with open("day2/input.txt", mode="r") as f:
    lines = f.read().splitlines()
    all_games = [process_lines(line) for line in lines]

actual_quantity = {"red": 12, "green": 13, "blue": 14}
valid_games = [id for id, game in all_games if game_valid(game, actual_quantity)]
game_powers = [
    get_power_of_quantities(bag)
    for bag in [get_min_quantities(game) for id, game in all_games]
]

print(sum(valid_games))
print(sum(game_powers))
