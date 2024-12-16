import re

from dataclasses import dataclass
from pathlib import Path

input_data = Path(__file__).parent.joinpath("input.txt").read_text()

INPUT_PATTERN = re.compile(
    r"Button A: X\+(?P<button_A_X>\d+), Y\+(?P<button_A_Y>\d+)\nButton B: X\+(?P<button_B_X>\d+), Y\+(?P<button_B_Y>\d+)\nPrize: X=(?P<prize_X>\d+), Y=(?P<prize_Y>\d+)\n",
)

A_PUSH_PRICE = 3
B_PUSH_PRICE = 1


@dataclass
class Machine:
    button_a_x: int
    button_a_y: int

    button_b_x: int
    button_b_y: int

    prize_x: int
    prize_y: int


machines = [
    Machine(
        int(match["button_A_X"]),
        int(match["button_A_Y"]),
        int(match["button_B_X"]),
        int(match["button_B_Y"]),
        int(match["prize_X"]),
        int(match["prize_Y"]),
    )
    for match in INPUT_PATTERN.finditer(input_data)
]


def get_possible_prize_winning_pushes(machine: Machine) -> list[tuple[int, int]]:
    solutions = []

    for a_pushes in range(0, 100):
        for b_pushes in range(0, 100):
            x = machine.button_a_x * a_pushes + machine.button_b_x * b_pushes
            y = machine.button_a_y * a_pushes + machine.button_b_y * b_pushes

            if x == machine.prize_x and y == machine.prize_y:
                solutions.append((a_pushes, b_pushes))

    return solutions


def get_solution_cost(solution: tuple[int, int]) -> int:
    a_pushes, b_pushes = solution
    return a_pushes * A_PUSH_PRICE + b_pushes * B_PUSH_PRICE


total_tokens_used = 0

for machine in machines:
    solutions = get_possible_prize_winning_pushes(machine)

    if not solutions:
        continue

    cheapest_solution_cost = min(get_solution_cost(solution) for solution in solutions)

    total_tokens_used += cheapest_solution_cost

print(total_tokens_used)
