from collections import defaultdict
import re


def de_word_string(string) -> str:
    conversion = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "zero": 0,
    }
    pattern = r"one|two|three|four|five|six|seven|eight|nine|zero"
    target = (
        str(conversion[match.group()]) if (match := re.search(pattern, string)) else -1
    )
    if target == -1:
        return string
    return de_word_string(re.sub(pattern, target, string, count=1, flags=re.IGNORECASE))


def get_calibration_value(string) -> int:
    numbers = [c for c in de_word_string(string) if c.isdigit()]
    return (
        int(numbers[0] + numbers[0])
        if len(numbers) == 1
        else int(numbers[0] + numbers[-1])
    )


with open("day1/input.txt", mode="r") as f:
    lines = f.read().splitlines()
    fixed = [get_calibration_value(line) for line in lines]

print(sum(fixed))
