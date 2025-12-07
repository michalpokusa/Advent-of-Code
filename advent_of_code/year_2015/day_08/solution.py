import json
from pathlib import Path

from advent_of_code import AdventOfCode


DEFAULT_EXAMPLE_INPUT_FILE_PATH = Path(__file__).parent.joinpath("example_input.txt")
DEFAULT_INPUT_FILE_PATH = Path(__file__).parent.joinpath("input.txt")


class AdventOfCode2015Day8Part1(AdventOfCode):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.strings = self.input_data.strip().split("\n")

    def get_answer(self):
        code_characters = 0
        characters_in_memory = 0

        for string in self.strings:
            code_characters += len(string)
            characters_in_memory += len(eval(string))

        return code_characters - characters_in_memory


class AdventOfCode2015Day8Part2(AdventOfCode2015Day8Part1):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def get_answer(self):
        code_characters = 0
        encoded_characters = 0

        for string in self.strings:
            code_characters += len(string)
            encoded_characters += len(json.dumps(string))

        return encoded_characters - code_characters


if __name__ == "__main__":
    answer = AdventOfCode2015Day8Part2(DEFAULT_INPUT_FILE_PATH).get_answer()
    print(answer)
