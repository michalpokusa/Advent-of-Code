from pathlib import Path

input_data = Path("./1/input.txt").read_text()

pairs = [
    [int(number) for number in line.strip().split("   ")]
    for line in input_data.split("\n")
    if line
]

left_side = [pair[0] for pair in pairs]
right_side = [pair[1] for pair in pairs]

total_similarity = 0

for index in range(len(pairs)):
    number = left_side[index]

    similarity = number * right_side.count(number)
    total_similarity += similarity

print(total_similarity)
