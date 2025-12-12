from itertools import product, pairwise
from pathlib import Path

from advent_of_code import AdventOfCode


DEFAULT_EXAMPLE_INPUT_FILE_PATH = Path(__file__).parent.joinpath("example_input.txt")
DEFAULT_INPUT_FILE_PATH = Path(__file__).parent.joinpath("input.txt")


class AdventOfCode2024Day10Part1(AdventOfCode):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.topographic_map = [
            [int(char) if char in "0123456789" else char for char in line]
            for line in self.input_data.split("\n")
            if line
        ]

    def is_inside_map(self, map: list[list[str]], y: int, x: int) -> bool:
        return 0 <= y < len(map) and 0 <= x < len(map[0])

    def get_trailhead_score(self, map: list[list[int]], y: int, x: int) -> int:

        # Check if the current cell is a height of 0
        if map[y][x] != 0:
            return 0

        trail_steps = {(y, x)}

        for height in range(1, 10):
            next_trail_steps = set()

            for y, x in trail_steps:

                # Up
                if self.is_inside_map(map, y - 1, x) and map[y - 1][x] == height:
                    next_trail_steps.add((y - 1, x))

                # Right
                if self.is_inside_map(map, y, x + 1) and map[y][x + 1] == height:
                    next_trail_steps.add((y, x + 1))

                # Down
                if self.is_inside_map(map, y + 1, x) and map[y + 1][x] == height:
                    next_trail_steps.add((y + 1, x))

                # Left
                if self.is_inside_map(map, y, x - 1) and map[y][x - 1] == height:
                    next_trail_steps.add((y, x - 1))

            trail_steps = next_trail_steps

            # There is no path from 0 to 9
            if not next_trail_steps:
                return 0

        return len(next_trail_steps)

    def get_answer(self):
        total_trailheads_score = 0

        for y in range(len(self.topographic_map)):
            for x in range(len(self.topographic_map[y])):
                total_trailheads_score += self.get_trailhead_score(
                    self.topographic_map, y, x
                )

        return total_trailheads_score


class AdventOfCode2024Day10Part2(AdventOfCode2024Day10Part1):

    def is_even_gradual_uphill_trail(self, trail: list[tuple[int, int]]) -> bool:
        for (y1, x1), (y2, x2) in pairwise(trail):
            if abs(y1 - y2) + abs(x1 - x2) != 1:
                return False

        return True

    def get_trailhead_rating(self, map: list[list[int]], y: int, x: int) -> int:

        # Check if the current cell is a height of 0
        if map[y][x] != 0:
            return 0

        all_trail_steps = {(0, y, x)}
        trail_steps = {(y, x)}

        for height in range(1, 10):
            next_trail_steps = set()

            for y, x in trail_steps:

                # Up
                if self.is_inside_map(map, y - 1, x) and map[y - 1][x] == height:
                    all_trail_steps.add((height, y - 1, x))
                    next_trail_steps.add((y - 1, x))

                # Right
                if self.is_inside_map(map, y, x + 1) and map[y][x + 1] == height:
                    all_trail_steps.add((height, y, x + 1))
                    next_trail_steps.add((y, x + 1))

                # Down
                if self.is_inside_map(map, y + 1, x) and map[y + 1][x] == height:
                    all_trail_steps.add((height, y + 1, x))
                    next_trail_steps.add((y + 1, x))

                # Left
                if self.is_inside_map(map, y, x - 1) and map[y][x - 1] == height:
                    all_trail_steps.add((height, y, x - 1))
                    next_trail_steps.add((y, x - 1))

            trail_steps = next_trail_steps

            # There is no path from 0 to 9
            if not next_trail_steps:
                return 0

        rating = 0
        trail_steps_by_height = []

        for height in range(10):
            trail_steps_by_height.append(
                {
                    (y, x)
                    for step_height, y, x in all_trail_steps
                    if step_height == height
                }
            )

        for distinct_trail in product(*trail_steps_by_height):
            if self.is_even_gradual_uphill_trail(distinct_trail):
                rating += 1

        return rating

    def get_answer(self):
        total_trailheads_rating = 0

        for y in range(len(self.topographic_map)):
            for x in range(len(self.topographic_map[y])):
                total_trailheads_rating += self.get_trailhead_rating(
                    self.topographic_map, y, x
                )

        return total_trailheads_rating


if __name__ == "__main__":
    answer = AdventOfCode2024Day10Part2(DEFAULT_INPUT_FILE_PATH).get_answer()
    print(answer)
