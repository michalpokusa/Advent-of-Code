from pathlib import Path

input_data = Path(__file__).parent.joinpath("input.txt").read_text()

topographic_map = [
    [int(char) if char in "0123456789" else char for char in line]
    for line in input_data.split("\n")
    if line
]


def is_inside_map(map: list[list[str]], y: int, x: int) -> bool:
    return 0 <= y < len(map) and 0 <= x < len(map[0])


def get_trailhead_score(map: list[list[int]], y: int, x: int) -> int:

    # Check if the current cell is a height of 0
    if map[y][x] != 0:
        return 0

    trail_steps = {(y, x)}

    for height in range(1, 10):
        next_trail_steps = set()

        for y, x in trail_steps:

            # Up
            if is_inside_map(map, y - 1, x) and map[y - 1][x] == height:
                next_trail_steps.add((y - 1, x))

            # Right
            if is_inside_map(map, y, x + 1) and map[y][x + 1] == height:
                next_trail_steps.add((y, x + 1))

            # Down
            if is_inside_map(map, y + 1, x) and map[y + 1][x] == height:
                next_trail_steps.add((y + 1, x))

            # Left
            if is_inside_map(map, y, x - 1) and map[y][x - 1] == height:
                next_trail_steps.add((y, x - 1))

        trail_steps = next_trail_steps

        if not next_trail_steps:
            return 0

    return len(next_trail_steps)


total_trailheads_score = 0

for y in range(len(topographic_map)):
    for x in range(len(topographic_map[y])):
        total_trailheads_score += get_trailhead_score(topographic_map, y, x)

print(total_trailheads_score)
