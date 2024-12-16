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
        # int(match["prize_X"]),
        # int(match["prize_Y"]),
        int(match["prize_X"]) + 10_000_000_000_000,
        int(match["prize_Y"]) + 10_000_000_000_000,
    )
    for match in INPUT_PATTERN.finditer(input_data)
]


def get_prize_winning_pushes(machine: Machine) -> tuple[int, int] | None:

    # a * ax + b * bx = px
    # a * ay + b * by = py

    ax = machine.button_a_x
    ay = machine.button_a_y
    bx = machine.button_b_x
    by = machine.button_b_y
    px = machine.prize_x
    py = machine.prize_y

    determinant = ax * by - ay * bx

    if determinant == 0:
        return None

    a = (px * by - py * bx) / determinant
    b = (ax * py - ay * px) / determinant

    if a >= 0 and b >= 0 and a.is_integer() and b.is_integer():
        return int(a), int(b)


def get_solution_cost(solution: tuple[int, int]) -> int:
    a_pushes, b_pushes = solution
    return a_pushes * A_PUSH_PRICE + b_pushes * B_PUSH_PRICE


total_tokens_used = 0

for machine in machines:
    solution = get_prize_winning_pushes(machine)

    if not solution:
        continue

    total_tokens_used += get_solution_cost(solution)

print(total_tokens_used)
