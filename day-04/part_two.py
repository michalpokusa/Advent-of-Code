from pathlib import Path


input_data = Path(__file__).parent.joinpath("input.txt").read_text()

matrix = [list(line) for line in input_data.splitlines()]

total_x_mas = 0

max_row = len(matrix)
max_col = len(matrix[0])

for row_nr in range(max_row):
    for col_nr in range(max_col):

        # M M      S M
        #  A   or   A    etc.
        # S S      M S
        try:
            assert matrix[row_nr][col_nr] == "A"

            assert 0 <= row_nr - 1 < max_row
            assert 0 <= row_nr + 1 < max_row
            assert 0 <= col_nr - 1 < max_row
            assert 0 <= col_nr + 1 < max_row

            left_top_to_right_bottom_diagonal = (
                matrix[row_nr - 1][col_nr - 1] + matrix[row_nr + 1][col_nr + 1]
            )
            assert left_top_to_right_bottom_diagonal in ["MS", "SM"]

            right_top_to_left_bottom_diagonal = (
                matrix[row_nr - 1][col_nr + 1] + matrix[row_nr + 1][col_nr - 1]
            )
            assert right_top_to_left_bottom_diagonal in ["MS", "SM"]

            # corners_together = "".join(
            #     [
            #         matrix[row_nr - 1][col_nr - 1],
            #         matrix[row_nr + 1][col_nr + 1],
            #         matrix[row_nr - 1][col_nr + 1],
            #         matrix[row_nr + 1][col_nr - 1],
            #     ]
            # )

            # assert matrix[row_nr][col_nr] == "A"
            # assert corners_together in [
            #     "MSMS",
            #     "MSSM",
            #     "SMMS",
            #     "SMSM",
            # ]

            # assert any(
            #     [
            #         matrix[row_nr - 1][col_nr -1] == "M" and matrix[row_nr + 1][col_nr + 1] == "S",
            #         matrix[row_nr - 1][col_nr -1] == "S" and matrix[row_nr + 1][col_nr + 1] == "M",
            #     ]
            # )
            # assert any(
            #     [
            #         matrix[row_nr + 1][col_nr - 1] == "M" and matrix[row_nr - 1][col_nr + 1] == "S",
            #         matrix[row_nr + 1][col_nr - 1] == "S" and matrix[row_nr - 1][col_nr + 1] == "M",
            #     ]
            # )

            total_x_mas += 1
        except AssertionError:
            pass


print(total_x_mas)
