from pathlib import Path

from advent_of_code import AdventOfCode


DEFAULT_EXAMPLE_INPUT_FILE_PATH = Path(__file__).parent.joinpath("example_input.txt")
DEFAULT_INPUT_FILE_PATH = Path(__file__).parent.joinpath("input.txt")


class AdventOfCode2015Day1Part1(AdventOfCode):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.instructions = list(self.input_data.strip())

    def get_answer(self):
        return self.instructions.count("(") - self.instructions.count(")")


class AdventOfCode2015Day1Part2(AdventOfCode2015Day1Part1):

    def get_answer(self):
        floor = 0
        for position, symbol in enumerate(self.instructions, 1):
            if symbol == "(":
                floor += 1
            elif symbol == ")":
                floor -= 1

            if floor == -1:
                return position


if __name__ == "__main__":
    answer = AdventOfCode2015Day1Part2(DEFAULT_INPUT_FILE_PATH).get_answer()
    print(answer)
