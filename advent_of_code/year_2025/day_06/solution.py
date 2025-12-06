import re

from pathlib import Path
from advent_of_code import AdventOfCode


DEFAULT_EXAMPLE_INPUT_FILE_PATH = Path(__file__).parent.joinpath("example_input.txt")
DEFAULT_INPUT_FILE_PATH = Path(__file__).parent.joinpath("input.txt")


class AdventOfCode2025Day6Part1(AdventOfCode):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        input_lines = self.input_data.strip().split("\n")

        self.numbers = [
            list(map(int, re.split(r"\s+", line.strip()))) for line in input_lines[:4]
        ]
        self.symbols = re.split(r"\s+", input_lines[4].strip())
        self.nr_of_problems = len(self.symbols)

    def get_answer(self):
        grand_total = 0

        for values in zip(*self.numbers, self.symbols):
            *numbers, symbol = values

            if symbol == "+":
                result = sum(numbers)
            elif symbol == "*":
                result = 1
                for number in numbers:
                    result *= number
            else:
                raise ValueError(f"Unknown symbol: {symbol}")

            grand_total += result

        return grand_total


class AdventOfCode2025Day6Part2(AdventOfCode):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.input_lines = [
            list(line.strip("\n")) for line in self.input_data.split("\n")
        ]

    def get_answer(self):
        columns = len(self.input_lines[0])

        grand_total = 0
        problem_symbol = None
        problem_numbers = []

        def add_problem_answer_to_grand_total():
            nonlocal grand_total, problem_symbol, problem_numbers

            if problem_symbol == "+":
                result = sum(problem_numbers)
            elif problem_symbol == "*":
                result = 1
                for number in problem_numbers:
                    result *= number
            else:
                raise ValueError(f"Unknown symbol: {problem_symbol}")

            grand_total += result

        def reset_problem():
            nonlocal problem_symbol, problem_numbers
            problem_symbol = None
            problem_numbers = []

        for col in range(columns):

            if (symbol := self.input_lines[-1][col]) in "+*":
                problem_symbol = symbol

            if all(
                self.input_lines[row][col] == " "
                for row in range(len(self.input_lines))
            ):
                add_problem_answer_to_grand_total()
                reset_problem()
                continue

            number = "".join(
                self.input_lines[row][col] for row in range(len(self.input_lines) - 1)
            ).strip()
            problem_numbers.append(int(number))

        add_problem_answer_to_grand_total()
        reset_problem()

        return grand_total


if __name__ == "__main__":
    answer = AdventOfCode2025Day6Part2(DEFAULT_INPUT_FILE_PATH).get_answer()
    print(answer)
