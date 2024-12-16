from itertools import product, pairwise
from pathlib import Path

input_data = Path(__file__).parent.joinpath("input.txt").read_text()

topographic_map = [
    [int(char) if char in "0123456789" else char for char in line]
    for line in input_data.split("\n")
    if line
]


def is_inside_map(map: list[list[str]], y: int, x: int) -> bool:
    return 0 <= y < len(map) and 0 <= x < len(map[0])


def is_even_gradual_uphill_trail(trail: list[tuple[int, int]]) -> bool:
    for (y1, x1), (y2, x2) in pairwise(trail):
        if abs(y1 - y2) + abs(x1 - x2) != 1:
            return False

    return True


def get_trailhead_rating(map: list[list[int]], y: int, x: int) -> int:

    # Check if the current cell is a height of 0
    if map[y][x] != 0:
        return 0

    all_trail_steps = {(0, y, x)}
    trail_steps = {(y, x)}

    for height in range(1, 10):
        next_trail_steps = set()

        for y, x in trail_steps:

            # Up
            if is_inside_map(map, y - 1, x) and map[y - 1][x] == height:
                all_trail_steps.add((height, y - 1, x))
                next_trail_steps.add((y - 1, x))

            # Right
            if is_inside_map(map, y, x + 1) and map[y][x + 1] == height:
                all_trail_steps.add((height, y, x + 1))
                next_trail_steps.add((y, x + 1))

            # Down
            if is_inside_map(map, y + 1, x) and map[y + 1][x] == height:
                all_trail_steps.add((height, y + 1, x))
                next_trail_steps.add((y + 1, x))

            # Left
            if is_inside_map(map, y, x - 1) and map[y][x - 1] == height:
                all_trail_steps.add((height, y, x - 1))
                next_trail_steps.add((y, x - 1))

        trail_steps = next_trail_steps

        # There is no path from 0 to 9
        if not next_trail_steps:
            return 0

    rating = 0
    trail_steps_by_height = []

    for height in range(10):
        trail_steps_by_height.append(
            {(y, x) for step_height, y, x in all_trail_steps if step_height == height}
        )

    for distinct_trail in product(*trail_steps_by_height):
        if is_even_gradual_uphill_trail(distinct_trail):
            rating += 1

    return rating


total_trailheads_rating = 0

for y in range(len(topographic_map)):
    for x in range(len(topographic_map[y])):
        total_trailheads_rating += get_trailhead_rating(topographic_map, y, x)

print(total_trailheads_rating)
