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


def number_valid(number: int, location: tuple[int, int], matrix: list[str]) -> bool:
    left_bound = max(location[1] - 1, 0)
    right_bound = min(location[1] + len(str(number)), len(matrix[0]) - 1)
    up_bound = max(location[0] - 1, 0)
    down_bound = min(location[0] + 1, len(matrix) - 1)

    for i in range(up_bound, down_bound + 1):
        for j in range(left_bound, right_bound + 1):
            if matrix[i][j] not in ".0123456789":
                return True
    return False


with open("day3/input.txt", mode="r") as f:
    lines = f.read().splitlines()
    all_numbers = get_all_numbers(lines)

print(
    sum(
        [value for key, value in all_numbers.items() if number_valid(value, key, lines)]
    )
)
