from itertools import product
from pathlib import Path

from advent_of_code import AdventOfCode


DEFAULT_EXAMPLE_INPUT_FILE_PATH = Path(__file__).parent.joinpath("example_input.txt")
DEFAULT_INPUT_FILE_PATH = Path(__file__).parent.joinpath("input.txt")


class AdventOfCode2024Day7Part1(AdventOfCode):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.equations = []
        for line in self.input_data.splitlines():
            test_value = int(line.split(": ")[0])
            numbers = [int(number) for number in line.split(": ")[1].split(" ")]

            self.equations.append((test_value, numbers))

    def get_possible_operators(self, how_many: int) -> list[str]:
        return product(["+", "*"], repeat=how_many)

    def combine_equation(
        self, test_value: int, numbers: list[int], operators: list[str]
    ) -> str:
        equation = f"{test_value} = {numbers[0]}"
        for number, operator in zip(numbers[1:], operators):
            equation += f" {operator} {number}"
        return equation

    def evaluates_left_to_right(self, test_value: int, numbers: list[int]) -> bool:
        for operators in self.get_possible_operators(len(numbers) - 1):
            result = numbers[0]

            for index, number in enumerate(numbers[1:]):
                if operators[index] == "+":
                    result += number
                elif operators[index] == "*":
                    result *= number

                if test_value < result:
                    break

            if test_value == result:
                return True

        return False

    def get_answer(self):
        total_calibration_result = 0

        for test_value, numbers in self.equations:
            if self.evaluates_left_to_right(test_value, numbers):
                total_calibration_result += test_value

        return total_calibration_result


class AdventOfCode2024Day7Part2(AdventOfCode2024Day7Part1):

    def get_possible_operators(self, how_many: int) -> list[str]:
        return product(["+", "*", "||"], repeat=how_many)

    def combine_equation_to_javascript(
        self, test_value: int, numbers: list[int], operators: list[str]
    ) -> str:
        equation = f"{numbers[0]}"
        for number, operator in zip(numbers[1:], operators):
            if operator == "+":
                equation = f"({equation} + {number})"
            elif operator == "*":
                equation = f"({equation} * {number})"
            elif operator == "||":
                equation = f"parseInt({equation} + '{number}')"
        return f'console.assert({test_value} === {equation}, "{equation}");'

    def evaluates_left_to_right(self, test_value: int, numbers: list[int]) -> bool:
        for operators in self.get_possible_operators(len(numbers) - 1):
            result = numbers[0]

            for index, number in enumerate(numbers[1:]):
                if operators[index] == "+":
                    result += number
                elif operators[index] == "*":
                    result *= number
                elif operators[index] == "||":
                    result = int(f"{result}{number}")

                if test_value < result:
                    break

            if test_value == result:
                return True

        return False


if __name__ == "__main__":
    answer = AdventOfCode2024Day7Part2(DEFAULT_INPUT_FILE_PATH).get_answer()
    print(answer)
