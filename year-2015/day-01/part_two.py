from pathlib import Path

input_data = Path(__file__).parent.joinpath("input.txt").read_text()


floor = 0

for position, symbol in enumerate(input_data, 1):
    if symbol == "(":
        floor += 1
    elif symbol == ")":
        floor -= 1

    if floor == -1:
        print(position)
        break
