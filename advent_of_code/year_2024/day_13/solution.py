import re
from dataclasses import dataclass
from pathlib import Path

from advent_of_code import AdventOfCode


DEFAULT_EXAMPLE_INPUT_FILE_PATH = Path(__file__).parent.joinpath("example_input.txt")
DEFAULT_INPUT_FILE_PATH = Path(__file__).parent.joinpath("input.txt")


@dataclass
class Machine:
    button_a_x: int
    button_a_y: int

    button_b_x: int
    button_b_y: int

    prize_x: int
    prize_y: int


class AdventOfCode2024Day13Part1(AdventOfCode):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        pattern = re.compile(
            r"Button A: X\+(?P<button_A_X>\d+), Y\+(?P<button_A_Y>\d+)\n"
            r"Button B: X\+(?P<button_B_X>\d+), Y\+(?P<button_B_Y>\d+)\n"
            r"Prize: X=(?P<prize_X>\d+), Y=(?P<prize_Y>\d+)\n",
        )

        self.a_push_price = 3
        self.b_push_price = 1

        self.machines = [
            Machine(
                int(match["button_A_X"]),
                int(match["button_A_Y"]),
                int(match["button_B_X"]),
                int(match["button_B_Y"]),
                int(match["prize_X"]),
                int(match["prize_Y"]),
            )
            for match in pattern.finditer(self.input_data)
        ]

    def get_possible_prize_winning_pushes(
        self, machine: Machine
    ) -> list[tuple[int, int]]:
        solutions = []

        for a_pushes in range(0, 100):
            for b_pushes in range(0, 100):
                x = machine.button_a_x * a_pushes + machine.button_b_x * b_pushes
                y = machine.button_a_y * a_pushes + machine.button_b_y * b_pushes

                if x == machine.prize_x and y == machine.prize_y:
                    solutions.append((a_pushes, b_pushes))

        return solutions

    def get_solution_cost(self, solution: tuple[int, int]) -> int:
        a_pushes, b_pushes = solution
        return a_pushes * self.a_push_price + b_pushes * self.b_push_price

    def get_answer(self):
        total_tokens_used = 0

        for machine in self.machines:
            solutions = self.get_possible_prize_winning_pushes(machine)

            if not solutions:
                continue

            cheapest_solution_cost = min(
                self.get_solution_cost(solution) for solution in solutions
            )

            total_tokens_used += cheapest_solution_cost

        return total_tokens_used


class AdventOfCode2024Day13Part2(AdventOfCode2024Day13Part1):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        for machine in self.machines:
            machine.prize_x += 10_000_000_000_000
            machine.prize_y += 10_000_000_000_000

    def get_prize_winning_pushes(self, machine: Machine) -> tuple[int, int] | None:

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

    def get_answer(self):
        total_tokens_used = 0

        for machine in self.machines:
            solution = self.get_prize_winning_pushes(machine)

            if not solution:
                continue

            total_tokens_used += self.get_solution_cost(solution)

        return total_tokens_used


if __name__ == "__main__":
    answer = AdventOfCode2024Day13Part2(DEFAULT_INPUT_FILE_PATH).get_answer()
    print(answer)
