from collections import Counter
from math import prod


def get_all_numbers(matrix: list[str]) -> dict[tuple[int, int], int]:
    numbers = {}
    number = ""
    coord = None
    for i, row in enumerate(matrix):
        for j, char in enumerate(row):
            if char.isdigit():
                number += char
                coord = (i, j) if not coord else coord
            elif number and coord:
                numbers.update({coord: int(number)})
                number = ""
                coord = None
        if number and coord:
            numbers.update({coord: int(number)})
            number = ""
            coord = None
    return numbers


def find_stars(
    number: int, location: tuple[int, int], matrix: list[str]
) -> tuple[tuple[int, int], int]:
    left_bound = max(location[1] - 1, 0)
    right_bound = min(location[1] + len(str(number)), len(matrix[0]) - 1)
    up_bound = max(location[0] - 1, 0)
    down_bound = min(location[0] + 1, len(matrix) - 1)

    for i in range(up_bound, down_bound + 1):
        for j in range(left_bound, right_bound + 1):
            if matrix[i][j] in "*":
                return (i, j), number


def gear_power(gear: tuple[int, int], all_stars: list[tuple[int, int], int]):
    numbers = [value for key, value in all_stars if key == gear]
    return prod(numbers)


with open("day3/test.txt", mode="r") as f:
    lines = f.read().splitlines()
    all_numbers = get_all_numbers(lines)

all_stars = [
    num
    for num in [find_stars(value, key, lines) for key, value in all_numbers.items()]
    if num
]
two_count_stars = [
    key for key, value in Counter(elem[0] for elem in all_stars).items() if value == 2
]
ratios = [gear_power(gear, all_stars) for gear in two_count_stars]
print(sum(ratios))
