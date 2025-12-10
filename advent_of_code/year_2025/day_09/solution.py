from itertools import combinations
from pathlib import Path
from advent_of_code import AdventOfCode


DEFAULT_EXAMPLE_INPUT_FILE_PATH = Path(__file__).parent.joinpath("example_input.txt")
DEFAULT_INPUT_FILE_PATH = Path(__file__).parent.joinpath("input.txt")


class AdventOfCode2025Day9Part1(AdventOfCode):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.red_tile_positions: list[tuple[int, int]] = [
            tuple(map(int, line.split(",")))
            for line in self.input_data.strip().splitlines()
        ]

    def get_rectangle_area(self, p1: tuple[int, int], p2: tuple[int, int]) -> int:
        x1, y1 = p1
        x2, y2 = p2
        return (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)

    def get_answer(self):
        largest_area = 0

        for p1, p2 in combinations(self.red_tile_positions, 2):
            area = self.get_rectangle_area(p1, p2)

            if area > largest_area:
                largest_area = area

        return largest_area


class AdventOfCode2025Day9Part2(AdventOfCode2025Day9Part1):

    def get_answer(self):
        raise NotImplementedError


if __name__ == "__main__":
    answer = AdventOfCode2025Day9Part2(DEFAULT_INPUT_FILE_PATH).get_answer()
    print(answer)
