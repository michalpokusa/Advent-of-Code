import re
from collections import defaultdict
from itertools import pairwise, permutations
from pathlib import Path

from advent_of_code import AdventOfCode


DEFAULT_EXAMPLE_INPUT_FILE_PATH = Path(__file__).parent.joinpath("example_input.txt")
DEFAULT_INPUT_FILE_PATH = Path(__file__).parent.joinpath("input.txt")


class AdventOfCode2015Day9Part1(AdventOfCode):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        records = re.findall(r"(\w+) to (\w+) = (\d+)", self.input_data)
        self.distances: dict[str, dict[str, int]] = defaultdict(dict)
        for start, end, distance in records:
            self.distances[start][end] = int(distance)
            self.distances[end][start] = int(distance)

        self.locations = set(self.distances.keys())

    def get_answer(self):
        shortest_distance = float("inf")

        for permutation in permutations(self.locations):
            distance = sum(
                self.distances[start][end] for start, end in pairwise(permutation)
            )

            shortest_distance = min(shortest_distance, distance)

        return shortest_distance


class AdventOfCode2015Day9Part2(AdventOfCode2015Day9Part1):

    def get_answer(self):
        longest_distance = 0

        for permutation in permutations(self.locations):
            distance = sum(
                self.distances[start][end] for start, end in pairwise(permutation)
            )

            longest_distance = max(longest_distance, distance)

        return longest_distance


if __name__ == "__main__":
    answer = AdventOfCode2015Day9Part2(DEFAULT_INPUT_FILE_PATH).get_answer()
    print(answer)
