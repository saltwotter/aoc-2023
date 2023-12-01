from collections import defaultdict
import re


def get_calibration_value(string) -> int:
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

    first_digit = (
        cap
        if (
            cap := re.search(
                r"(\d|one|two|three|four|five|six|seven|eight|nine|zero)",
                string,
                flags=re.IGNORECASE,
            ).groups()[0]
        ).isdigit()
        else str(conversion[cap])
    )
    last_digit = (
        cap
        if (
            cap := re.search(
                r".*(\d|one|two|three|four|five|six|seven|eight|nine)",
                string,
                flags=re.IGNORECASE,
            ).groups()[0]
        ).isdigit()
        else str(conversion[cap])
    )
    print(first_digit + last_digit)
    return int(first_digit + last_digit)


with open("day1/input.txt", mode="r") as f:
    lines = f.read().splitlines()
    fixed = [get_calibration_value(line) for line in lines]

print(sum(fixed))
