import json

from pathlib import Path


input_data = Path(__file__).parent.joinpath("input.txt").read_text()

lines = [line for line in input_data.split("\n") if line]

total_encoded_characters = 0

for line in lines:

    encoded_line = json.dumps(line)

    total_encoded_characters += len(encoded_line) - len(line)

print(total_encoded_characters)
