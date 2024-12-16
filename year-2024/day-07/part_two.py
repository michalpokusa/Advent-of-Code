from pathlib import Path
from itertools import product

input_data = Path(__file__).parent.joinpath("input.txt").read_text()

equations = []
for line in input_data.splitlines():

    test_value = int(line.split(": ")[0])
    numbers = [int(number) for number in line.split(": ")[1].split(" ")]

    equations.append((test_value, numbers))


def get_possible_operators(how_many: int) -> list[str]:
    return product(["+", "*", "||"], repeat=how_many)


def combine_equation(test_value: int, numbers: list[int], operators: list[str]) -> str:
    equation = f"{test_value} = {numbers[0]}"
    for number, operator in zip(numbers[1:], operators):
        equation += f" {operator} {number}"
    return equation


def combine_equation_to_javascript(
    test_value: int, numbers: list[int], operators: list[str]
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


def evaluates_left_to_right(test_value: int, numbers: list[int]) -> bool:
    for operators in get_possible_operators(len(numbers) - 1):
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
            print(combine_equation(test_value, numbers, operators))
            # print(combine_equation_to_javascript(test_value, numbers, operators))
            return True

    return False


total_calibration_result = 0

for test_value, numbers in equations:
    if evaluates_left_to_right(test_value, numbers):
        total_calibration_result += test_value

print(total_calibration_result)
