from collections import defaultdict
from pathlib import Path

input_data = Path(__file__).parent.joinpath("input.txt").read_text()

directions = list(input_data.strip())

santa_x, santa_y = 0, 0
robo_santa_x, robo_santa_y = 0, 0

houses = defaultdict(int)
houses[(santa_x, santa_y)] += 1
houses[(robo_santa_x, robo_santa_y)] += 1

while True:

    if not directions:
        break

    direction = directions.pop(0)

    if direction == "^":
        santa_y -= 1
    elif direction == "v":
        santa_y += 1
    elif direction == ">":
        santa_x += 1
    elif direction == "<":
        santa_x -= 1

    houses[(santa_x, santa_y)] += 1

    if not directions:
        break

    direction = directions.pop(0)

    if direction == "^":
        robo_santa_y -= 1
    elif direction == "v":
        robo_santa_y += 1
    elif direction == ">":
        robo_santa_x += 1
    elif direction == "<":
        robo_santa_x -= 1

    houses[(robo_santa_x, robo_santa_y)] += 1

houses_with_more_than_one_present = sum(
    1 for presents in houses.values() if presents >= 1
)

print(houses_with_more_than_one_present)
