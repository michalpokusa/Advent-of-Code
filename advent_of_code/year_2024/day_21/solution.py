from pathlib import Path

from advent_of_code import AdventOfCode


DEFAULT_EXAMPLE_INPUT_FILE_PATH = Path(__file__).parent.joinpath("example_input.txt")
DEFAULT_INPUT_FILE_PATH = Path(__file__).parent.joinpath("input.txt")


# [Numeric keypad] (depressurized)
# ↑
# [Directional keypad 1] (high levels of radiation)
# ↑
# [Directional keypad 2] (-40 degrees)
# ↑
# [Directional keypad 3] (full of Historians) ← You type here


# Numeric keypad
# +---+---+---+
# | 7 | 8 | 9 |
# +---+---+---+
# | 4 | 5 | 6 |
# +---+---+---+
# | 1 | 2 | 3 |
# +---+---+---+
#     | 0 | A |
#     +---+---+
class NumericKeypad:

    def __init__(self):
        self.keypad = [
            ["7", "8", "9"],
            ["4", "5", "6"],
            ["1", "2", "3"],
            [None, "0", "A"],
        ]
        self.arm_location = (3, 2)


# Directional keypad
#     +---+---+
#     | ^ | A |
# +---+---+---+
# | < | v | > |
# +---+---+---+
class DirectionalKeypad:

    def __init__(self):
        self.keypad = [
            [None, "^", "A"],
            ["<", "v", ">"],
        ]
        self.arm_location = (0, 2)


class AdventOfCode2024Day21Part1(AdventOfCode):

    def get_answer(self):
        raise NotImplementedError


class AdventOfCode2024Day22Part2(AdventOfCode2024Day21Part1):

    def get_answer(self):
        raise NotImplementedError


if __name__ == "__main__":
    answer = AdventOfCode2024Day21Part1(DEFAULT_INPUT_FILE_PATH).get_answer()
    print(answer)
