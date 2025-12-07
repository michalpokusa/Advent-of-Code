import re
from pathlib import Path

from advent_of_code import AdventOfCode


DEFAULT_EXAMPLE_INPUT_FILE_PATH = Path(__file__).parent.joinpath("example_input.txt")
DEFAULT_INPUT_FILE_PATH = Path(__file__).parent.joinpath("input.txt")


class AdventOfCode2015Day6Part1(AdventOfCode):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.lights = [[False for _ in range(1000)] for _ in range(1000)]
        self.instructions = re.findall(
            r"(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)",
            self.input_data,
        )

    def get_lights_range(self, y1: int, x1: int, y2: int, x2: int):
        for y in range(y1, y2 + 1):
            for x in range(x1, x2 + 1):
                yield y, x

    def get_answer(self):
        for operation, y1, x1, y2, x2 in self.instructions:
            y1, x1, y2, x2 = map(int, (y1, x1, y2, x2))

            if operation == "turn on":
                for y, x in self.get_lights_range(y1, x1, y2, x2):
                    self.lights[y][x] = True
            elif operation == "turn off":
                for y, x in self.get_lights_range(y1, x1, y2, x2):
                    self.lights[y][x] = False
            elif operation == "toggle":
                for y, x in self.get_lights_range(y1, x1, y2, x2):
                    self.lights[y][x] = not self.lights[y][x]
            else:
                raise ValueError(f"Unknown operation: {operation}")

        return sum(1 for row in self.lights for light in row if light is True)


class AdventOfCode2015Day6Part2(AdventOfCode2015Day6Part1):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.brightness = [[0 for _ in range(1000)] for _ in range(1000)]

    def get_answer(self):
        for operation, y1, x1, y2, x2 in self.instructions:
            y1, x1, y2, x2 = map(int, (y1, x1, y2, x2))

            if operation == "turn on":
                for y, x in self.get_lights_range(y1, x1, y2, x2):
                    self.brightness[y][x] += 1
            elif operation == "turn off":
                for y, x in self.get_lights_range(y1, x1, y2, x2):
                    self.brightness[y][x] = max(0, self.brightness[y][x] - 1)
            elif operation == "toggle":
                for y, x in self.get_lights_range(y1, x1, y2, x2):
                    self.brightness[y][x] += 2
            else:
                raise ValueError(f"Unknown operation: {operation}")

        return sum(brightness for row in self.brightness for brightness in row)


if __name__ == "__main__":
    answer = AdventOfCode2015Day6Part2(DEFAULT_INPUT_FILE_PATH).get_answer()
    print(answer)
