from pathlib import Path
from advent_of_code import AdventOfCode


DEFAULT_EXAMPLE_INPUT_FILE_PATH = Path(__file__).parent.joinpath("example_input.txt")
DEFAULT_INPUT_FILE_PATH = Path(__file__).parent.joinpath("input.txt")


class AdventOfCode2025Day7Part1(AdventOfCode):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.manifold = [
            list(line.strip()) for line in self.input_data.strip().splitlines()
        ]

    def print_manifold(self, margin: int = 0) -> None:
        for line in self.manifold:
            print("".join(line))
        print("\n" * margin, end="")

    def get_answer(self):
        times_beam_splits = 0

        width = len(self.manifold[0])
        height = len(self.manifold)

        for y in range(height):
            for x in range(width):

                if self.manifold[y][x] == "S":
                    self.manifold[y + 1][x] = "|"
                    continue

                if self.manifold[y][x] == "." and self.manifold[y - 1][x] == "|":
                    self.manifold[y][x] = "|"
                    continue

                if self.manifold[y][x] == "^" and self.manifold[y - 1][x] == "|":
                    splited = False
                    if 0 <= x - 1 < width and self.manifold[y][x - 1] in [".", "|"]:
                        self.manifold[y][x - 1] = "|"
                        splited = True

                    if 0 <= x + 1 < width and self.manifold[y][x + 1] in [".", "|"]:
                        self.manifold[y][x + 1] = "|"
                        splited = True

                    if splited:
                        times_beam_splits += 1
                    continue

        self.print_manifold(margin=1)

        return times_beam_splits


class AdventOfCode2025Day7Part2(AdventOfCode2025Day7Part1):

    def get_answer(self):
        width = len(self.manifold[0])
        height = len(self.manifold)

        for y in range(height):
            for x in range(width):

                if self.manifold[y][x] in "S^":
                    continue

                if self.manifold[y - 1][x] == "S":
                    self.manifold[y][x] = 1
                    continue

                self.manifold[y][x] = 0

                if type(self.manifold[y - 1][x]) is int:
                    self.manifold[y][x] += self.manifold[y - 1][x]

                for dx in [-1, 1]:
                    if (
                        0 <= x + dx < width
                        and self.manifold[y][x + dx] == "^"
                        and type(self.manifold[y - 1][x + dx]) is int
                    ):
                        self.manifold[y][x] += self.manifold[y - 1][x + dx]

        return sum(self.manifold[-1])


if __name__ == "__main__":
    answer = AdventOfCode2025Day7Part2(DEFAULT_EXAMPLE_INPUT_FILE_PATH).get_answer()
    print(answer)
