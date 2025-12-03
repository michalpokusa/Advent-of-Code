import re

from pathlib import Path
from advent_of_code import AdventOfCode


DEFAULT_EXAMPLE_INPUT_FILE_PATH = Path(__file__).parent.joinpath("example_input.txt")
DEFAULT_INPUT_FILE_PATH = Path(__file__).parent.joinpath("input.txt")


class AdventOfCode2025Day2Part1(AdventOfCode):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.id_ranges = [
            id_range.split("-") for id_range in self.input_data.split(",")
        ]

    @staticmethod
    def id_is_valid(id: str) -> bool:

        if len(id) % 2 == 0:
            half = len(id) // 2
            if id[:half] == id[half:]:
                return False

        return True

    def get_answer(self) -> int:
        invalid_ids = [
            id
            for first_id, last_id in self.id_ranges
            for id in range(int(first_id), int(last_id) + 1)
            if not self.id_is_valid(str(id))
        ]

        return sum(map(int, invalid_ids))


class AdventOfCode2025Day2Part2(AdventOfCode2025Day2Part1):

    @staticmethod
    def id_is_valid(id: str) -> bool:
        return re.fullmatch(r"^(\d+)\1+$", id) is None


answer = AdventOfCode2025Day2Part2(DEFAULT_INPUT_FILE_PATH).get_answer()
print(answer)
