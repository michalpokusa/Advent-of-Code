import re

from pathlib import Path

PATTERN = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)")

input_data = Path(__file__).parent.joinpath("input.txt").read_text()

matches = PATTERN.finditer(input_data)

mul_enabled = True
total = 0

for match in matches:

    if match.group() == "do()":
        mul_enabled = True
        continue

    if match.group() == "don't()":
        mul_enabled = False
        continue

    if not mul_enabled:
        continue

    number1 = match.group(1)
    number2 = match.group(2)

    total += int(number1) * int(number2)

print(total)
