from collections import defaultdict
from pathlib import Path
from itertools import combinations

input_data = Path(__file__).parent.joinpath("input.txt").read_text()

map = [[char for char in line] for line in input_data.split("\n") if line]

antennas: "dict[str, set[tuple[int, int]]]" = defaultdict(set)

for row_idx, row in enumerate(map):
    for col_idx, col in enumerate(row):
        if col != ".":
            antennas[col].add((row_idx, col_idx))


def is_inside_map(map: list[list[str]], y: int, x: int) -> bool:
    return 0 <= y < len(map) and 0 <= x < len(map[0])


antinodes: "dict[str, set[tuple[int, int]]]" = defaultdict(set)

for antenna, positions in antennas.items():
    for pos1, pos2 in combinations(positions, 2):
        d_row = pos2[0] - pos1[0]
        d_col = pos2[1] - pos1[1]

        antinode_pos = pos1
        while is_inside_map(map, *antinode_pos):
            antinodes[antenna].add(antinode_pos)

            antinode_pos = (antinode_pos[0] - d_row, antinode_pos[1] - d_col)

        antinode_pos = pos2
        while is_inside_map(map, *antinode_pos):
            antinodes[antenna].add(antinode_pos)

            antinode_pos = (antinode_pos[0] + d_row, antinode_pos[1] + d_col)


unique_antinodes = set(
    position for positions in antinodes.values() for position in positions
)


print(len(unique_antinodes))
