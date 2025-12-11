from pathlib import Path

from advent_of_code import AdventOfCode


DEFAULT_EXAMPLE_INPUT_FILE_PATH = Path(__file__).parent.joinpath("example_input.txt")
DEFAULT_INPUT_FILE_PATH = Path(__file__).parent.joinpath("input.txt")


class AdventOfCode2024Day4Part1(AdventOfCode):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.matrix = [list(line) for line in self.input_data.splitlines()]
        self.max_row = len(self.matrix)
        self.max_col = len(self.matrix[0])

    def get_answer(self):
        total_xmas = 0

        for row_nr in range(self.max_row):
            for col_nr in range(self.max_col):

                # XMAS
                try:
                    assert 0 <= col_nr + 1 < self.max_col
                    assert 0 <= col_nr + 2 < self.max_col
                    assert 0 <= col_nr + 3 < self.max_col

                    assert self.matrix[row_nr][col_nr] == "X"
                    assert self.matrix[row_nr][col_nr + 1] == "M"
                    assert self.matrix[row_nr][col_nr + 2] == "A"
                    assert self.matrix[row_nr][col_nr + 3] == "S"

                    total_xmas += 1
                except AssertionError:
                    pass

                # X
                #  M
                #   A
                #    S
                try:
                    assert 0 <= row_nr + 1 < self.max_row
                    assert 0 <= col_nr + 1 < self.max_col
                    assert 0 <= row_nr + 2 < self.max_row
                    assert 0 <= col_nr + 2 < self.max_col
                    assert 0 <= row_nr + 3 < self.max_row
                    assert 0 <= col_nr + 3 < self.max_col

                    assert self.matrix[row_nr][col_nr] == "X"
                    assert self.matrix[row_nr + 1][col_nr + 1] == "M"
                    assert self.matrix[row_nr + 2][col_nr + 2] == "A"
                    assert self.matrix[row_nr + 3][col_nr + 3] == "S"

                    total_xmas += 1
                except AssertionError:
                    pass

                # X
                # M
                # A
                # S
                try:
                    assert 0 <= row_nr + 1 < self.max_row
                    assert 0 <= row_nr + 2 < self.max_row
                    assert 0 <= row_nr + 3 < self.max_row

                    assert self.matrix[row_nr][col_nr] == "X"
                    assert self.matrix[row_nr + 1][col_nr] == "M"
                    assert self.matrix[row_nr + 2][col_nr] == "A"
                    assert self.matrix[row_nr + 3][col_nr] == "S"

                    total_xmas += 1
                except AssertionError:
                    pass

                #    X
                #   M
                #  A
                # S
                try:
                    assert 0 <= row_nr + 1 < self.max_row
                    assert 0 <= col_nr - 1 < self.max_col
                    assert 0 <= row_nr + 2 < self.max_row
                    assert 0 <= col_nr - 2 < self.max_col
                    assert 0 <= row_nr + 3 < self.max_row
                    assert 0 <= col_nr - 3 < self.max_col

                    assert self.matrix[row_nr][col_nr] == "X"
                    assert self.matrix[row_nr + 1][col_nr - 1] == "M"
                    assert self.matrix[row_nr + 2][col_nr - 2] == "A"
                    assert self.matrix[row_nr + 3][col_nr - 3] == "S"

                    total_xmas += 1
                except AssertionError:
                    pass

                # SAMX
                try:
                    assert 0 <= col_nr - 1 < self.max_col
                    assert 0 <= col_nr - 2 < self.max_col
                    assert 0 <= col_nr - 3 < self.max_col

                    assert self.matrix[row_nr][col_nr] == "X"
                    assert self.matrix[row_nr][col_nr - 1] == "M"
                    assert self.matrix[row_nr][col_nr - 2] == "A"
                    assert self.matrix[row_nr][col_nr - 3] == "S"

                    total_xmas += 1
                except AssertionError:
                    pass

                # S
                #  A
                #   M
                #    X
                try:
                    assert 0 <= row_nr - 1 < self.max_row
                    assert 0 <= col_nr - 1 < self.max_col
                    assert 0 <= row_nr - 2 < self.max_row
                    assert 0 <= col_nr - 2 < self.max_col
                    assert 0 <= row_nr - 3 < self.max_row
                    assert 0 <= col_nr - 3 < self.max_col

                    assert self.matrix[row_nr][col_nr] == "X"
                    assert self.matrix[row_nr - 1][col_nr - 1] == "M"
                    assert self.matrix[row_nr - 2][col_nr - 2] == "A"
                    assert self.matrix[row_nr - 3][col_nr - 3] == "S"

                    total_xmas += 1
                except AssertionError:
                    pass

                # S
                # A
                # M
                # X
                try:
                    assert 0 <= row_nr - 1 < self.max_row
                    assert 0 <= row_nr - 2 < self.max_row
                    assert 0 <= row_nr - 3 < self.max_row

                    assert self.matrix[row_nr][col_nr] == "X"
                    assert self.matrix[row_nr - 1][col_nr] == "M"
                    assert self.matrix[row_nr - 2][col_nr] == "A"
                    assert self.matrix[row_nr - 3][col_nr] == "S"

                    total_xmas += 1
                except AssertionError:
                    pass

                #    S
                #   A
                #  M
                # X
                try:
                    assert 0 <= row_nr - 1 < self.max_row
                    assert 0 <= col_nr + 1 < self.max_col
                    assert 0 <= row_nr - 2 < self.max_row
                    assert 0 <= col_nr + 2 < self.max_col
                    assert 0 <= row_nr - 3 < self.max_row
                    assert 0 <= col_nr + 3 < self.max_col

                    assert self.matrix[row_nr][col_nr] == "X"
                    assert self.matrix[row_nr - 1][col_nr + 1] == "M"
                    assert self.matrix[row_nr - 2][col_nr + 2] == "A"
                    assert self.matrix[row_nr - 3][col_nr + 3] == "S"

                    total_xmas += 1
                except AssertionError:
                    pass

        return total_xmas


class AdventOfCode2024Day4Part2(AdventOfCode2024Day4Part1):

    def get_answer(self):
        total_x_mas = 0

        for row_nr in range(self.max_row):
            for col_nr in range(self.max_col):

                # M M      S M
                #  A   or   A    etc.
                # S S      M S
                try:
                    assert self.matrix[row_nr][col_nr] == "A"

                    assert 0 <= row_nr - 1 < self.max_row
                    assert 0 <= row_nr + 1 < self.max_row
                    assert 0 <= col_nr - 1 < self.max_col
                    assert 0 <= col_nr + 1 < self.max_col

                    left_top_to_right_bottom_diagonal = (
                        self.matrix[row_nr - 1][col_nr - 1]
                        + self.matrix[row_nr + 1][col_nr + 1]
                    )
                    assert left_top_to_right_bottom_diagonal in ["MS", "SM"]

                    right_top_to_left_bottom_diagonal = (
                        self.matrix[row_nr - 1][col_nr + 1]
                        + self.matrix[row_nr + 1][col_nr - 1]
                    )
                    assert right_top_to_left_bottom_diagonal in ["MS", "SM"]

                    total_x_mas += 1
                except AssertionError:
                    pass

        return total_x_mas


if __name__ == "__main__":
    answer = AdventOfCode2024Day4Part2(DEFAULT_INPUT_FILE_PATH).get_answer()
    print(answer)
