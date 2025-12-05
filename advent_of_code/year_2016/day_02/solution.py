from pathlib import Path
from advent_of_code import AdventOfCode


DEFAULT_EXAMPLE_INPUT_FILE_PATH = Path(__file__).parent.joinpath("example_input.txt")
DEFAULT_INPUT_FILE_PATH = Path(__file__).parent.joinpath("input.txt")


KEYPAD1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
KEYPAD2 = [
    [None, None, 1, None, None],
    [None, 2, 3, 4, None],
    [5, 6, 7, 8, 9],
    [None, "A", "B", "C", None],
    [None, None, "D", None, None],
]


class AdventOfCode2016Day2Part1(AdventOfCode):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.instructions = [
            list(line) for line in self.input_data.strip().splitlines()
        ]

    def get_answer(self) -> int:
        x, y = 1, 1
        bathroom_code = ""

        for moves_sequence in self.instructions:

            for move in moves_sequence:
                match move:
                    case "U":
                        y = max(0, y - 1)
                    case "D":
                        y = min(2, y + 1)
                    case "L":
                        x = max(0, x - 1)
                    case "R":
                        x = min(2, x + 1)

            bathroom_code += str(KEYPAD1[y][x])

        return bathroom_code


class AdventOfCode2016Day2Part2(AdventOfCode2016Day2Part1):

    def get_answer(self) -> int:
        x, y = 0, 2
        bathroom_code = ""

        for moves_sequence in self.instructions:

            for move in moves_sequence:
                next_x, next_y = x, y

                match move:
                    case "U":
                        next_y = max(0, y - 1)
                    case "D":
                        next_y = min(4, y + 1)
                    case "L":
                        next_x = max(0, x - 1)
                    case "R":
                        next_x = min(4, x + 1)

                if KEYPAD2[next_y][next_x] is not None:
                    x, y = next_x, next_y

            bathroom_code += str(KEYPAD2[y][x])

        return bathroom_code


if __name__ == "__main__":
    answer = AdventOfCode2016Day2Part2(DEFAULT_INPUT_FILE_PATH).get_answer()
    print(answer)
