from pathlib import Path

input_data = Path(__file__).parent.joinpath("input.txt").read_text()

lights = [[0 for _ in range(1000)] for _ in range(1000)]

instructions = [instruction for instruction in input_data.split("\n") if instruction]


def get_lights_range(y1: int, x1: int, y2: int, x2: int):
    for y in range(y1, y2 + 1):
        for x in range(x1, x2 + 1):
            yield y, x


for instruction in instructions:

    y1, x1, y2, x2 = (
        int(number)
        for number in (
            instruction.replace("turn on ", "")
            .replace("turn off ", "")
            .replace("toggle ", "")
            .replace(" through ", ",")
            .split(",")
        )
    )

    if "turn on" in instruction:
        for y, x in get_lights_range(y1, x1, y2, x2):
            lights[y][x] += 1
    elif "turn off" in instruction:
        for y, x in get_lights_range(y1, x1, y2, x2):
            lights[y][x] = 0 if lights[y][x] == 0 else lights[y][x] - 1
    elif "toggle" in instruction:
        for y, x in get_lights_range(y1, x1, y2, x2):
            lights[y][x] += 2


total_brightness = sum(brightness for row in lights for brightness in row)

print(total_brightness)
