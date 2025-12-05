import re
from pathlib import Path

from advent_of_code import AdventOfCode


DEFAULT_EXAMPLE_INPUT_FILE_PATH = Path(__file__).parent.joinpath("example_input.txt")
DEFAULT_INPUT_FILE_PATH = Path(__file__).parent.joinpath("input.txt")


class AdventOfCode2016Day8Part1(AdventOfCode):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.sequences = self.input_data.strip().splitlines()

        # self.screen = [["." for _ in range(7)] for _ in range(3)]
        self.screen = [["." for _ in range(50)] for _ in range(6)]

    def rect(self, x: int, y: int) -> None:
        for row in range(y):
            for col in range(x):
                self.screen[row][col] = "#"

    def rotate_row(self, y: int, by: int) -> None:
        assert by < len(self.screen[0])

        state = self.screen[y][:]
        new_state = state[-by:] + state[:-by]
        self.screen[y] = new_state

    def rotate_column(self, x: int, by: int) -> None:
        assert by < len(self.screen)

        state = [self.screen[row][x] for row in range(len(self.screen))]
        new_state = state[-by:] + state[:-by]

        for row in range(len(self.screen)):
            self.screen[row][x] = new_state[row]

    def print_screen(self) -> None:
        for row in self.screen:
            print("".join(row))

    def apply_sequence_onto_screen(self) -> None:
        for sequence in self.sequences:
            if match := re.match(r"rect (\d+)x(\d+)", sequence):
                x, y = map(int, match.groups())
                self.rect(x, y)
            elif match := re.match(r"rotate row y=(\d+) by (\d+)", sequence):
                y, by = map(int, match.groups())
                self.rotate_row(y, by)
            elif match := re.match(r"rotate column x=(\d+) by (\d+)", sequence):
                x, by = map(int, match.groups())
                self.rotate_column(x, by)

    def get_answer(self):
        self.apply_sequence_onto_screen()
        return sum(1 for row in self.screen for pixel in row if pixel == "#")


class AdventOfCode2016Day8Part2(AdventOfCode2016Day8Part1):

    def get_answer(self):
        self.apply_sequence_onto_screen()
        return "\n".join("".join(row).replace(".", " ") for row in self.screen)


if __name__ == "__main__":
    answer = AdventOfCode2016Day8Part2(DEFAULT_INPUT_FILE_PATH).get_answer()
    print(answer)
