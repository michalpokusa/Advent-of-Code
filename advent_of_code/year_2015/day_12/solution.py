import re
import json
from pathlib import Path

from advent_of_code import AdventOfCode


DEFAULT_EXAMPLE_INPUT_FILE_PATH = Path(__file__).parent.joinpath("example_input.txt")
DEFAULT_INPUT_FILE_PATH = Path(__file__).parent.joinpath("input.txt")


class AdventOfCode2015Day12Part1(AdventOfCode):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.json_document = self.input_data.strip().splitlines()[0]

    def get_answer(self):
        return sum(
            int(match.group(0)) for match in re.finditer(r"-?\d+", self.json_document)
        )


class AdventOfCode2015Day12Part2(AdventOfCode2015Day12Part1):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.parsed_json = json.loads(self.json_document)

    def sum_of_all_numbers(self, element: int | str | list | dict) -> int:
        if isinstance(element, int):
            return element

        elif isinstance(element, str):
            return 0

        elif isinstance(element, list):
            return sum(self.sum_of_all_numbers(item) for item in element)

        elif isinstance(element, dict):
            if "red" in element.values():
                return 0

            return sum(self.sum_of_all_numbers(item) for item in element.values())

        raise ValueError("Unsupported type")

    def get_answer(self):
        return self.sum_of_all_numbers(self.parsed_json)


if __name__ == "__main__":
    answer = AdventOfCode2015Day12Part2(DEFAULT_INPUT_FILE_PATH).get_answer()
    print(answer)
