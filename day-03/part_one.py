import re

from pathlib import Path

PATTERN = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")

input_data = Path("./3/input.txt").read_text()

matches = PATTERN.finditer(input_data)

total = 0

for match in matches:
    print(match)

    number1 = match.group(1)
    number2 = match.group(2)

    total += int(number1) * int(number2)

print(total)
