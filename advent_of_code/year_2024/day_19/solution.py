import re
from pathlib import Path

from advent_of_code import AdventOfCode


DEFAULT_EXAMPLE_INPUT_FILE_PATH = Path(__file__).parent.joinpath("example_input.txt")
DEFAULT_INPUT_FILE_PATH = Path(__file__).parent.joinpath("input.txt")


class AdventOfCode2024Day19Part1(AdventOfCode):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        towel_patterns_data, desired_designs_data = self.input_data.split("\n\n")

        self.towel_patterns = [pattern for pattern in towel_patterns_data.split(", ")]
        self.desired_designs = [
            design for design in desired_designs_data.split("\n") if design
        ]
        self.possible_design_pattern = re.compile(
            f"^({'|'.join(self.towel_patterns)})+$"
        )

    def get_answer(self):
        possible_designs = 0

        for design in self.desired_designs:
            if re.fullmatch(self.possible_design_pattern, design):
                possible_designs += 1

        return possible_designs


def cache_by(key):

    def decorator(function):
        storage: dict[str, int] = {}

        def wrapper(*args, **kwargs):
            cache_key = key(*args, **kwargs)
            if cache_key in storage:
                return storage[cache_key]
            result = function(*args, **kwargs)
            storage[cache_key] = result
            return result

        return wrapper

    return decorator


class AdventOfCode2024Day19Part2(AdventOfCode2024Day19Part1):

    @cache_by(key=lambda *args, **kwargs: args[1])
    def number_of_ways(self, design: str, towel_patterns: list[str]) -> int:
        total_ways = 0

        for pattern in towel_patterns:
            if design == pattern:
                total_ways += 1
            elif design.startswith(pattern):
                total_ways += self.number_of_ways(
                    design[len(pattern) :], towel_patterns
                )

        return total_ways

    def get_answer(self):
        total_different_ways = 0

        for design in self.desired_designs:
            total_different_ways += self.number_of_ways(design, self.towel_patterns)

        return total_different_ways


if __name__ == "__main__":
    answer = AdventOfCode2024Day19Part2(DEFAULT_INPUT_FILE_PATH).get_answer()
    print(answer)
