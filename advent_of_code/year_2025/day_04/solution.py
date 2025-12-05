from copy import deepcopy

from pathlib import Path
from advent_of_code import AdventOfCode


DEFAULT_EXAMPLE_INPUT_FILE_PATH = Path(__file__).parent.joinpath("example_input.txt")
DEFAULT_INPUT_FILE_PATH = Path(__file__).parent.joinpath("input.txt")


class AdventOfCode2025Day4Part1(AdventOfCode):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.diagram = [list(line) for line in self.input_data.strip().split("\n")]
        self.diagram_width = len(self.diagram[0])
        self.diagram_height = len(self.diagram)

        self.diagram_copy = deepcopy(self.diagram)

    def get_answer(self):
        accessible_rolls_of_paper = 0

        for x in range(self.diagram_width):
            for y in range(self.diagram_height):

                if self.diagram[y][x] != "@":
                    continue

                adjacent_rolls = 0

                for dx, dy in [
                    (-1, -1),  # top-left
                    (0, -1),  # top
                    (1, -1),  # top-right
                    (-1, 0),  # left
                    (1, 0),  # right
                    (-1, 1),  # bottom-left
                    (0, 1),  # bottom
                    (1, 1),  # bottom-right
                ]:

                    if (x + dx) < 0 or self.diagram_width <= (x + dx):
                        continue
                    if (y + dy) < 0 or self.diagram_height <= (y + dy):
                        continue

                    if self.diagram[y + dy][x + dx] == "@":
                        adjacent_rolls += 1

                if adjacent_rolls < 4:
                    accessible_rolls_of_paper += 1
                    self.diagram_copy[y][x] = "x"

        return accessible_rolls_of_paper


class AdventOfCode2025Day4Part2(AdventOfCode2025Day4Part1):

    def print_diagram(self, diagram: list[list[str]]) -> None:
        for line in diagram:
            print("".join(line))

    def unmark_removed_rolls_of_paper(self, diagram: list[list[str]]) -> None:
        for x in range(self.diagram_width):
            for y in range(self.diagram_height):
                if diagram[y][x] == "x":
                    diagram[y][x] = "."

    def remove_accessible_rolls_of_paper(self) -> None:
        removed_rolls_of_paper = 0

        for x in range(self.diagram_width):
            for y in range(self.diagram_height):

                if self.diagram[y][x] != "@":
                    continue

                adjacent_rolls = 0

                for dx, dy in [
                    (-1, -1),  # top-left
                    (0, -1),  # top
                    (1, -1),  # top-right
                    (-1, 0),  # left
                    (1, 0),  # right
                    (-1, 1),  # bottom-left
                    (0, 1),  # bottom
                    (1, 1),  # bottom-right
                ]:

                    if (x + dx) < 0 or self.diagram_width <= (x + dx):
                        continue
                    if (y + dy) < 0 or self.diagram_height <= (y + dy):
                        continue

                    if self.diagram[y + dy][x + dx] == "@":
                        adjacent_rolls += 1

                if adjacent_rolls < 4:
                    removed_rolls_of_paper += 1
                    self.diagram[y][x] = "x"

        print(f"Removed {removed_rolls_of_paper} rolls of paper:")
        self.print_diagram(self.diagram)
        print()
        self.unmark_removed_rolls_of_paper(self.diagram)

        return removed_rolls_of_paper

    def get_answer(self):
        total_removed_rolls_of_paper = 0

        while True:
            removed_rolls_this_repeat = self.remove_accessible_rolls_of_paper()
            total_removed_rolls_of_paper += removed_rolls_this_repeat

            if removed_rolls_this_repeat == 0:
                break

        return total_removed_rolls_of_paper


if __name__ == "__main__":
    answer = AdventOfCode2025Day4Part2(DEFAULT_EXAMPLE_INPUT_FILE_PATH).get_answer()
    print(answer)
