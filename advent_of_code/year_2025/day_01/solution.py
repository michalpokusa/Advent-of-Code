from pathlib import Path
from advent_of_code import AdventOfCode


DEFAULT_EXAMPLE_INPUT_FILE_PATH = Path(__file__).parent.joinpath("example_input.txt")
DEFAULT_INPUT_FILE_PATH = Path(__file__).parent.joinpath("input.txt")


class AdventOfCode2025Day1Part1(AdventOfCode):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.rotations = [line.strip() for line in self.input_data.strip().splitlines()]

    def get_answer(self) -> int:
        current_position = 50
        nr_of_times_pointing_to_zero = 0

        for rotation in self.rotations:
            direction = rotation[0]
            distance = int(rotation[1:])

            if direction == "R":
                current_position += distance
            elif direction == "L":
                current_position -= distance

            while current_position < 0:
                current_position += 100
            while current_position >= 100:
                current_position -= 100

            if current_position == 0:
                nr_of_times_pointing_to_zero += 1

        return nr_of_times_pointing_to_zero


class AdventOfCode2025Day1Part2(AdventOfCode2025Day1Part1):

    def get_answer(self) -> int:
        current_position = 50
        nr_of_times_pointing_to_zero = 0

        for rotation in self.rotations:
            direction = rotation[0]
            distance = int(rotation[1:])

            for _ in range(distance):
                current_position += 1 if direction == "R" else -1

                if current_position < 0:
                    current_position += 100
                elif current_position >= 100:
                    current_position -= 100

                if current_position == 0:
                    nr_of_times_pointing_to_zero += 1

        return nr_of_times_pointing_to_zero


if __name__ == "__main__":
    answer = AdventOfCode2025Day1Part1(DEFAULT_EXAMPLE_INPUT_FILE_PATH).get_answer()
    print(answer)
