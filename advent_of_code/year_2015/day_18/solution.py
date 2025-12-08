from itertools import product
from pathlib import Path

from advent_of_code import AdventOfCode


DEFAULT_EXAMPLE_INPUT_FILE_PATH = Path(__file__).parent.joinpath("example_input.txt")
DEFAULT_INPUT_FILE_PATH = Path(__file__).parent.joinpath("input.txt")


class AdventOfCode2015Day18Part1(AdventOfCode):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.state = [
            [[light, None] for light in line]
            for line in self.input_data.strip().splitlines()
        ]

    def calculate_state_changes(self):
        for y, x in product(range(len(self.state)), repeat=2):

            neighbors_on = 0

            for dy, dx in product([-1, 0, 1], repeat=2):
                if dy == 0 and dx == 0:
                    continue

                if (
                    0 <= y + dy < len(self.state)
                    and 0 <= x + dx < len(self.state)
                    and self.state[y + dy][x + dx][0] == "#"
                ):
                    neighbors_on += 1

            if self.state[y][x][0] == "#":
                self.state[y][x][1] = "#" if neighbors_on in (2, 3) else "."
            else:
                self.state[y][x][1] = "#" if neighbors_on == 3 else "."

    def apply_state_changes(self):
        for y, x in product(range(len(self.state)), repeat=2):
            self.state[y][x][0] = self.state[y][x][1]

    def reset_state_changes(self):
        for y, x in product(range(len(self.state)), repeat=2):
            self.state[y][x][1] = None

    def print_state(self):
        for line in self.state:
            print("".join(light[0] for light in line))
        print()

    def step(self):
        self.calculate_state_changes()
        self.apply_state_changes()
        self.reset_state_changes()
        self.print_state()

    def get_answer(self):
        for _ in range(100):
            self.step()

        return sum(1 for row in self.state for light in row if light[0] == "#")


class AdventOfCode2015Day18Part2(AdventOfCode2015Day18Part1):

    def turn_on_corners(self):
        for y, x in product([0, len(self.state) - 1], repeat=2):
            self.state[y][x][0] = "#"

    def step(self):
        self.turn_on_corners()
        self.calculate_state_changes()
        self.apply_state_changes()
        self.reset_state_changes()
        self.turn_on_corners()
        self.print_state()


if __name__ == "__main__":
    answer = AdventOfCode2015Day18Part2(DEFAULT_INPUT_FILE_PATH).get_answer()
    print(answer)
