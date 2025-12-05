import re

from itertools import batched
from pathlib import Path

from advent_of_code import AdventOfCode


DEFAULT_EXAMPLE_INPUT_FILE_PATH = Path(__file__).parent.joinpath("example_input.txt")
DEFAULT_INPUT_FILE_PATH = Path(__file__).parent.joinpath("input.txt")


class AdventOfCode2016Day3Part1(AdventOfCode):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.triangle_sides = [
            list(map(int, re.findall(r"\d+", line)))
            for line in self.input_data.strip().splitlines()
        ]

    def get_answer(self):
        possible_triangles = 0

        for sides in self.triangle_sides:
            a, b, c = sorted(sides)

            if a + b > c:
                possible_triangles += 1

        return possible_triangles


class AdventOfCode2016Day3Part2(AdventOfCode2016Day3Part1):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.triangle_sides = [
            sides
            for triangle1, triangle2, triangle3 in batched(self.triangle_sides, 3)
            for sides in zip(triangle1, triangle2, triangle3)
        ]


if __name__ == "__main__":
    answer = AdventOfCode2016Day3Part2(DEFAULT_INPUT_FILE_PATH).get_answer()
    print(answer)
