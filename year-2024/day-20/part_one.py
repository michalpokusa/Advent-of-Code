from collections import defaultdict
from pathlib import Path

input_data = Path(__file__).parent.joinpath("input.txt").read_text()

racetrack_map = [list(line) for line in input_data.split("\n") if line]


def get_starting_position(racetrack_map: list[list[str]]) -> tuple[int, int]:
    for y in range(len(racetrack_map)):
        for x in range(len(racetrack_map[y])):
            if racetrack_map[y][x] == "S":
                return y, x
    raise ValueError("No starting position found")


starting_position = get_starting_position(racetrack_map)


def get_picoseconds_to_reach_end(
    racetrack_map: list[list[str]],
    starting_position: tuple[int, int],
) -> int:
    start_y, start_x = starting_position

    positions_to_check = set([(start_y, start_x, 0)])

    while positions_to_check:
        y, x, picoseconds = positions_to_check.pop()

        # Right
        if racetrack_map[y][x + 1] == ".":
            racetrack_map[y][x + 1] = picoseconds + 1
            positions_to_check.add((y, x + 1, picoseconds + 1))

        # Down
        if racetrack_map[y + 1][x] == ".":
            racetrack_map[y + 1][x] = picoseconds + 1
            positions_to_check.add((y + 1, x, picoseconds + 1))

        # Left
        if racetrack_map[y][x - 1] == ".":
            racetrack_map[y][x - 1] = picoseconds + 1
            positions_to_check.add((y, x - 1, picoseconds + 1))

        # Up
        if racetrack_map[y - 1][x] == ".":
            racetrack_map[y - 1][x] = picoseconds + 1
            positions_to_check.add((y - 1, x, picoseconds + 1))

        if "E" in (
            racetrack_map[y][x + 1],
            racetrack_map[y + 1][x],
            racetrack_map[y][x - 1],
            racetrack_map[y - 1][x],
        ):
            return picoseconds + 1


no_cheat_picoseconds = get_picoseconds_to_reach_end(racetrack_map, starting_position)

CHEATS = defaultdict(int)

total_iterations = (len(racetrack_map) - 2) * (len(racetrack_map[0]) - 2)

for cheat_y in range(1, len(racetrack_map) - 1):
    for cheat_x in range(1, len(racetrack_map[0]) - 1):

        iteration_nr = (cheat_y - 1) * (len(racetrack_map[0]) - 2) + (cheat_x)
        print(f"{iteration_nr}/{total_iterations}", end="\r")

        if racetrack_map[cheat_y][cheat_x] != "#":
            continue

        cheated_racetrack_map = [list(line) for line in input_data.split("\n") if line]
        cheated_racetrack_map[cheat_y][cheat_x] = "."

        cheated_picoseconds = get_picoseconds_to_reach_end(
            cheated_racetrack_map, starting_position
        )

        if cheated_picoseconds < no_cheat_picoseconds:
            saved_picoseconds = no_cheat_picoseconds - cheated_picoseconds

            CHEATS[saved_picoseconds] += 1


cheats_that_save_more_than_100_picoseconds = sum(
    count for picoseconds, count in CHEATS.items() if picoseconds >= 100
)

print()
print(cheats_that_save_more_than_100_picoseconds)
