from collections import defaultdict
from itertools import combinations
from pathlib import Path

from advent_of_code import AdventOfCode


DEFAULT_EXAMPLE_INPUT_FILE_PATH = Path(__file__).parent.joinpath("example_input.txt")
DEFAULT_INPUT_FILE_PATH = Path(__file__).parent.joinpath("input.txt")


class AdventOfCode2024Day8Part1(AdventOfCode):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.map = [
            [char for char in line] for line in self.input_data.split("\n") if line
        ]

        self.antennas: dict[str, set[tuple[int, int]]] = defaultdict(set)
        for row_idx, row in enumerate(self.map):
            for col_idx, col in enumerate(row):
                if col != ".":
                    self.antennas[col].add((row_idx, col_idx))

    def is_inside_map(self, map: list[list[str]], y: int, x: int) -> bool:
        return 0 <= y < len(map) and 0 <= x < len(map[0])

    def get_answer(self):
        antinodes: dict[str, set[tuple[int, int]]] = defaultdict(set)

        for antenna, positions in self.antennas.items():
            for pos1, pos2 in combinations(positions, 2):
                d_row = pos2[0] - pos1[0]
                d_col = pos2[1] - pos1[1]

                antinode_pos1 = (pos1[0] - d_row, pos1[1] - d_col)
                antinode_pos2 = (pos2[0] + d_row, pos2[1] + d_col)

                if self.is_inside_map(self.map, *antinode_pos1):
                    antinodes[antenna].add(antinode_pos1)
                if self.is_inside_map(self.map, *antinode_pos2):
                    antinodes[antenna].add(antinode_pos2)

        unique_antinodes = set(
            position for positions in antinodes.values() for position in positions
        )

        return len(unique_antinodes)


class AdventOfCode2024Day8Part2(AdventOfCode2024Day8Part1):

    def get_answer(self):
        antinodes: dict[str, set[tuple[int, int]]] = defaultdict(set)

        for antenna, positions in self.antennas.items():
            for pos1, pos2 in combinations(positions, 2):
                d_row = pos2[0] - pos1[0]
                d_col = pos2[1] - pos1[1]

                antinode_pos = pos1
                while self.is_inside_map(self.map, *antinode_pos):
                    antinodes[antenna].add(antinode_pos)
                    antinode_pos = (antinode_pos[0] - d_row, antinode_pos[1] - d_col)

                antinode_pos = pos2
                while self.is_inside_map(self.map, *antinode_pos):
                    antinodes[antenna].add(antinode_pos)
                    antinode_pos = (antinode_pos[0] + d_row, antinode_pos[1] + d_col)

        unique_antinodes = set(
            position for positions in antinodes.values() for position in positions
        )

        return len(unique_antinodes)


if __name__ == "__main__":
    answer = AdventOfCode2024Day8Part2(DEFAULT_INPUT_FILE_PATH).get_answer()
    print(answer)
