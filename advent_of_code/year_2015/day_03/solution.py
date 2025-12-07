from collections import defaultdict
from pathlib import Path

from advent_of_code import AdventOfCode


DEFAULT_EXAMPLE_INPUT_FILE_PATH = Path(__file__).parent.joinpath("example_input.txt")
DEFAULT_INPUT_FILE_PATH = Path(__file__).parent.joinpath("input.txt")


class AdventOfCode2015Day3Part1(AdventOfCode):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.directions = list(self.input_data.strip())

    def get_answer(self):
        santa_x, santa_y = 0, 0

        houses = defaultdict(int)
        houses[(santa_x, santa_y)] += 1

        for direction in self.directions:
            if direction == "^":
                santa_y -= 1
            elif direction == "v":
                santa_y += 1
            elif direction == ">":
                santa_x += 1
            elif direction == "<":
                santa_x -= 1

            houses[(santa_x, santa_y)] += 1

        return len(houses)


class AdventOfCode2015Day3Part2(AdventOfCode2015Day3Part1):

    def get_answer(self):
        santa_x, santa_y = 0, 0
        robo_santa_x, robo_santa_y = 0, 0

        houses = defaultdict(int)
        houses[(santa_x, santa_y)] += 1
        houses[(robo_santa_x, robo_santa_y)] += 1

        while True:

            if not self.directions:
                break

            direction = self.directions.pop(0)

            if direction == "^":
                santa_y -= 1
            elif direction == "v":
                santa_y += 1
            elif direction == ">":
                santa_x += 1
            elif direction == "<":
                santa_x -= 1

            houses[(santa_x, santa_y)] += 1

            if not self.directions:
                break

            direction = self.directions.pop(0)

            if direction == "^":
                robo_santa_y -= 1
            elif direction == "v":
                robo_santa_y += 1
            elif direction == ">":
                robo_santa_x += 1
            elif direction == "<":
                robo_santa_x -= 1

            houses[(robo_santa_x, robo_santa_y)] += 1

        return len(houses)


if __name__ == "__main__":
    answer = AdventOfCode2015Day3Part2(DEFAULT_INPUT_FILE_PATH).get_answer()
    print(answer)
