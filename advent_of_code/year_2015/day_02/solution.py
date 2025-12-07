from pathlib import Path

from advent_of_code import AdventOfCode


DEFAULT_EXAMPLE_INPUT_FILE_PATH = Path(__file__).parent.joinpath("example_input.txt")
DEFAULT_INPUT_FILE_PATH = Path(__file__).parent.joinpath("input.txt")


class AdventOfCode2015Day2Part1(AdventOfCode):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.dimensions = [
            tuple(map(int, line.split("x")))
            for line in self.input_data.strip().splitlines()
        ]

    def get_answer(self):
        total_wrapping_paper_square_feet = 0

        for l, w, h in self.dimensions:
            box_area = (2 * l * w) + (2 * w * h) + (2 * h * l)
            slack = min(l * w, w * h, h * l)
            total_wrapping_paper_square_feet += box_area + slack

        return total_wrapping_paper_square_feet


class AdventOfCode2015Day2Part2(AdventOfCode2015Day2Part1):

    def get_answer(self):
        total_ribbon_feet = 0

        for l, w, h in self.dimensions:
            perimeters = [2 * (l + w), 2 * (w + h), 2 * (h + l)]
            bow = l * w * h
            total_ribbon_feet += min(perimeters) + bow

        return total_ribbon_feet


if __name__ == "__main__":
    answer = AdventOfCode2015Day2Part2(DEFAULT_INPUT_FILE_PATH).get_answer()
    print(answer)
