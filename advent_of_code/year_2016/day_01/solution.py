from pathlib import Path
from advent_of_code import AdventOfCode


DEFAULT_EXAMPLE_INPUT_FILE_PATH = Path(__file__).parent.joinpath("example_input.txt")
DEFAULT_INPUT_FILE_PATH = Path(__file__).parent.joinpath("input.txt")


DIRECTION_CHANGES = {
    "N": {
        "R": "E",
        "L": "W",
    },
    "E": {
        "R": "S",
        "L": "N",
    },
    "S": {
        "R": "W",
        "L": "E",
    },
    "W": {
        "R": "N",
        "L": "S",
    },
}


class AdventOfCode2016Day1Part1(AdventOfCode):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.instructions = self.input_data.strip().split(", ")

    def get_answer(self):
        x, y = 0, 0
        facing = "N"

        for instruction in self.instructions:
            turn, steps = instruction[0], int(instruction[1:])

            facing = DIRECTION_CHANGES[facing][turn]

            match facing:
                case "N":
                    y += steps
                case "E":
                    x += steps
                case "S":
                    y -= steps
                case "W":
                    x -= steps

        return abs(x) + abs(y)


class AdventOfCode2016Day1Part2(AdventOfCode2016Day1Part1):

    def get_answer(self):
        x, y = 0, 0
        facing = "N"

        visited_locations = set()

        for instruction in self.instructions:
            turn, steps = instruction[0], int(instruction[1:])

            facing = DIRECTION_CHANGES[facing][turn]

            for _ in range(steps):
                match facing:
                    case "N":
                        y += 1
                    case "E":
                        x += 1
                    case "S":
                        y -= 1
                    case "W":
                        x -= 1

                location = (x, y)

                if location in visited_locations:
                    return abs(x) + abs(y)

                visited_locations.add(location)


if __name__ == "__main__":
    answer = AdventOfCode2016Day1Part2(DEFAULT_INPUT_FILE_PATH).get_answer()
    print(answer)
