from pathlib import Path

input_data = Path(__file__).parent.joinpath("input.txt").read_text()


floor = 0

floors_up = input_data.count("(")
floors_down = input_data.count(")")

print(floors_up - floors_down)
