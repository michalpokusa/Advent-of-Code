from itertools import combinations
from pathlib import Path

from advent_of_code import AdventOfCode


DEFAULT_EXAMPLE_INPUT_FILE_PATH = Path(__file__).parent.joinpath("example_input.txt")
DEFAULT_INPUT_FILE_PATH = Path(__file__).parent.joinpath("input.txt")


class AdventOfCode2015Day17Part1(AdventOfCode):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.containers = list(map(int, self.input_data.strip().splitlines()))

    def get_answer(self):
        target_volume = 150
        valid_combinations = 0

        for containers_number in range(1, len(self.containers) + 1):
            for containers_combination in combinations(
                self.containers, containers_number
            ):
                if sum(containers_combination) == target_volume:
                    valid_combinations += 1

        return valid_combinations


class AdventOfCode2015Day17Part2(AdventOfCode2015Day17Part1):

    def get_answer(self):
        target_volume = 150
        valid_combinations = 0

        for containers_number in range(1, len(self.containers) + 1):

            if valid_combinations > 0:
                break

            for containers_combination in combinations(
                self.containers, containers_number
            ):
                if sum(containers_combination) == target_volume:
                    valid_combinations += 1

        return valid_combinations


if __name__ == "__main__":
    answer = AdventOfCode2015Day17Part2(DEFAULT_INPUT_FILE_PATH).get_answer()
    print(answer)
