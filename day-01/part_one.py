from pathlib import Path

input_data = Path(__file__).parent.joinpath("input.txt").read_text()

pairs = [
    [int(number) for number in line.strip().split("   ")]
    for line in input_data.split("\n")
    if line
]

left_side = [pair[0] for pair in pairs]
right_side = [pair[1] for pair in pairs]

sorted_left_side = sorted(left_side)
sorted_right_side = sorted(right_side)

total_distance_between_pairs = 0

for index in range(len(pairs)):
    distance_between_pairs = abs(sorted_left_side[index] - sorted_right_side[index])
    total_distance_between_pairs += distance_between_pairs

print(total_distance_between_pairs)
