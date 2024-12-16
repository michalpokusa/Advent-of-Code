from pathlib import Path

input_data = Path(__file__).parent.joinpath("input.txt").read_text()

lines = (line.strip() for line in input_data.split("\n") if line)


total_ribbon_feet = 0

for line in lines:
    dimensions = line.split("x")
    length, width, height = (int(dimension) for dimension in dimensions)

    perimeters = [2 * (length + width), 2 * (width + height), 2 * (height + length)]
    bow = length * width * height

    total_ribbon_feet += min(perimeters) + bow

print(total_ribbon_feet)
