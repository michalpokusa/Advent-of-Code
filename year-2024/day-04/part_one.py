from pathlib import Path


input_data = Path(__file__).parent.joinpath("input.txt").read_text()

matrix = [list(line) for line in input_data.splitlines()]

total_xmas = 0

max_row = len(matrix)
max_col = len(matrix[0])

for row_nr in range(max_row):
    for col_nr in range(max_col):

        # XMAS
        try:
            assert 0 <= col_nr + 1 < max_col
            assert 0 <= col_nr + 2 < max_col
            assert 0 <= col_nr + 3 < max_col

            assert matrix[row_nr][col_nr] == "X"
            assert matrix[row_nr][col_nr + 1] == "M"
            assert matrix[row_nr][col_nr + 2] == "A"
            assert matrix[row_nr][col_nr + 3] == "S"

            total_xmas += 1
        except AssertionError:
            pass

        # X
        #  M
        #   A
        #    S
        try:
            assert 0 <= row_nr + 1 < max_row
            assert 0 <= col_nr + 1 < max_col
            assert 0 <= row_nr + 2 < max_row
            assert 0 <= col_nr + 2 < max_col
            assert 0 <= row_nr + 3 < max_row
            assert 0 <= col_nr + 3 < max_col

            assert matrix[row_nr][col_nr] == "X"
            assert matrix[row_nr + 1][col_nr + 1] == "M"
            assert matrix[row_nr + 2][col_nr + 2] == "A"
            assert matrix[row_nr + 3][col_nr + 3] == "S"

            total_xmas += 1
        except AssertionError:
            pass

        # X
        # M
        # A
        # S
        try:
            assert 0 <= row_nr + 1 < max_row
            assert 0 <= row_nr + 2 < max_row
            assert 0 <= row_nr + 3 < max_row

            assert matrix[row_nr][col_nr] == "X"
            assert matrix[row_nr + 1][col_nr] == "M"
            assert matrix[row_nr + 2][col_nr] == "A"
            assert matrix[row_nr + 3][col_nr] == "S"

            total_xmas += 1
        except AssertionError:
            pass

        #    X
        #   M
        #  A
        # S
        try:
            assert 0 <= row_nr + 1 < max_row
            assert 0 <= col_nr - 1 < max_col
            assert 0 <= row_nr + 2 < max_row
            assert 0 <= col_nr - 2 < max_col
            assert 0 <= row_nr + 3 < max_row
            assert 0 <= col_nr - 3 < max_col

            assert matrix[row_nr][col_nr] == "X"
            assert matrix[row_nr + 1][col_nr - 1] == "M"
            assert matrix[row_nr + 2][col_nr - 2] == "A"
            assert matrix[row_nr + 3][col_nr - 3] == "S"

            total_xmas += 1
        except AssertionError:
            pass

        # SAMX
        try:
            assert 0 <= col_nr - 1 < max_col
            assert 0 <= col_nr - 2 < max_col
            assert 0 <= col_nr - 3 < max_col

            assert matrix[row_nr][col_nr] == "X"
            assert matrix[row_nr][col_nr - 1] == "M"
            assert matrix[row_nr][col_nr - 2] == "A"
            assert matrix[row_nr][col_nr - 3] == "S"

            total_xmas += 1
        except AssertionError:
            pass

        # S
        #  A
        #   M
        #    X
        try:
            assert 0 <= row_nr - 1 < max_row
            assert 0 <= col_nr - 1 < max_col
            assert 0 <= row_nr - 2 < max_row
            assert 0 <= col_nr - 2 < max_col
            assert 0 <= row_nr - 3 < max_row
            assert 0 <= col_nr - 3 < max_col

            assert matrix[row_nr][col_nr] == "X"
            assert matrix[row_nr - 1][col_nr - 1] == "M"
            assert matrix[row_nr - 2][col_nr - 2] == "A"
            assert matrix[row_nr - 3][col_nr - 3] == "S"

            total_xmas += 1
        except AssertionError:
            pass

        # S
        # A
        # M
        # X
        try:
            assert 0 <= row_nr - 1 < max_row
            assert 0 <= row_nr - 2 < max_row
            assert 0 <= row_nr - 3 < max_row

            assert matrix[row_nr][col_nr] == "X"
            assert matrix[row_nr - 1][col_nr] == "M"
            assert matrix[row_nr - 2][col_nr] == "A"
            assert matrix[row_nr - 3][col_nr] == "S"

            total_xmas += 1
        except AssertionError:
            pass

        #    S
        #   A
        #  M
        # X
        try:
            assert 0 <= row_nr - 1 < max_row
            assert 0 <= col_nr + 1 < max_col
            assert 0 <= row_nr - 2 < max_row
            assert 0 <= col_nr + 2 < max_col
            assert 0 <= row_nr - 3 < max_row
            assert 0 <= col_nr + 3 < max_col

            assert matrix[row_nr][col_nr] == "X"
            assert matrix[row_nr - 1][col_nr + 1] == "M"
            assert matrix[row_nr - 2][col_nr + 2] == "A"
            assert matrix[row_nr - 3][col_nr + 3] == "S"

            total_xmas += 1
        except AssertionError:
            pass


print(total_xmas)
