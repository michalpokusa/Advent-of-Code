from hashlib import md5
from pathlib import Path

from advent_of_code import AdventOfCode


DEFAULT_EXAMPLE_INPUT_FILE_PATH = Path(__file__).parent.joinpath("example_input.txt")
DEFAULT_INPUT_FILE_PATH = Path(__file__).parent.joinpath("input.txt")


class AdventOfCode2015Day4Part1(AdventOfCode):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.secret_key = self.input_data.strip()

    prefix = "00000"

    def get_answer(self):
        number = 1
        while True:
            hash = md5(f"{self.secret_key}{number}".encode()).hexdigest()

            if hash.startswith(self.prefix):
                return number

            number += 1


class AdventOfCode2015Day4Part2(AdventOfCode2015Day4Part1):

    prefix = "000000"


if __name__ == "__main__":
    answer = AdventOfCode2015Day4Part2(DEFAULT_INPUT_FILE_PATH).get_answer()
    print(answer)
