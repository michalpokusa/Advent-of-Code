from collections import defaultdict
from pathlib import Path

input_data = Path(__file__).parent.joinpath("input.txt").read_text()

directions = list(input_data.strip())

santa_x, santa_y = 0, 0

houses = defaultdict(int)
houses[(santa_x, santa_y)] += 1

for direction in directions:
    if direction == "^":
        santa_y -= 1
    elif direction == "v":
        santa_y += 1
    elif direction == ">":
        santa_x += 1
    elif direction == "<":
        santa_x -= 1

    houses[(santa_x, santa_y)] += 1

houses_with_more_than_one_present = sum(
    1 for presents in houses.values() if presents >= 1
)

print(houses_with_more_than_one_present)
