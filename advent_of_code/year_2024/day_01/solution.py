from pathlib import Path

from advent_of_code import AdventOfCode


DEFAULT_EXAMPLE_INPUT_FILE_PATH = Path(__file__).parent.joinpath("example_input.txt")
DEFAULT_INPUT_FILE_PATH = Path(__file__).parent.joinpath("input.txt")


class AdventOfCode2024Day1Part1(AdventOfCode):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.pairs = [
            [int(number) for number in line.strip().split("   ")]
            for line in self.input_data.split("\n")
            if line
        ]
        self.left_side = [pair[0] for pair in self.pairs]
        self.right_side = [pair[1] for pair in self.pairs]

    def get_answer(self):
        sorted_left_side = sorted(self.left_side)
        sorted_right_side = sorted(self.right_side)

        total_distance_between_pairs = 0

        for index in range(len(self.pairs)):
            distance_between_pairs = abs(
                sorted_left_side[index] - sorted_right_side[index]
            )
            total_distance_between_pairs += distance_between_pairs

        return total_distance_between_pairs


class AdventOfCode2024Day1Part2(AdventOfCode2024Day1Part1):

    def get_answer(self):
        total_similarity = 0

        for number in self.left_side:
            similarity = number * self.right_side.count(number)
            total_similarity += similarity

        return total_similarity


if __name__ == "__main__":
    answer = AdventOfCode2024Day1Part2(DEFAULT_INPUT_FILE_PATH).get_answer()
    print(answer)
