from pathlib import Path

input_data = Path(__file__).parent.joinpath("input.txt").read_text()

rotations = input_data.strip().splitlines()

current_position = 50
nr_of_times_pointing_to_zero = 0

for rotation in rotations:
    direction = rotation[0]
    distance = int(rotation[1:])

    if direction == "R":
        current_position += distance
    elif direction == "L":
        current_position -= distance

    while current_position < 0:
        current_position += 100
    while current_position >= 100:
        current_position -= 100

    if current_position == 0:
        nr_of_times_pointing_to_zero += 1

print(nr_of_times_pointing_to_zero)
