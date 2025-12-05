from collections import defaultdict
from pathlib import Path

from advent_of_code import AdventOfCode


DEFAULT_EXAMPLE_INPUT_FILE_PATH = Path(__file__).parent.joinpath("example_input.txt")
DEFAULT_INPUT_FILE_PATH = Path(__file__).parent.joinpath("input.txt")


class AdventOfCode2016Day6Part1(AdventOfCode):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.message_signals = self.input_data.strip().splitlines()

    most_likely = True

    def get_answer(self):
        columns = len(self.message_signals[0])

        positions = [defaultdict(int) for _ in range(columns)]

        for signal in self.message_signals:
            for index, letter in enumerate(signal):
                positions[index][letter] += 1

        password_letters = [
            sorted(
                position.items(), key=lambda item: item[1], reverse=self.most_likely
            )[0][0]
            for position in positions
        ]

        return "".join(password_letters)


class AdventOfCode2016Day6Part2(AdventOfCode2016Day6Part1):

    most_likely = False


if __name__ == "__main__":
    answer = AdventOfCode2016Day6Part2(DEFAULT_INPUT_FILE_PATH).get_answer()
    print(answer)
