from pathlib import Path

input_data = Path(__file__).parent.joinpath("input.txt").read_text()

lines = (line.strip() for line in input_data.split("\n") if line)

total_square_feet = 0

for line in lines:
    dimensions = line.split("x")
    length, width, height = (int(dimension) for dimension in dimensions)

    sides = [length * width, width * height, height * length]
    slack = min(sides)

    total_square_feet += 2 * sum(sides) + slack

print(total_square_feet)
