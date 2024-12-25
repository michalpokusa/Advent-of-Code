import re

from pathlib import Path

input_data = Path(__file__).parent.joinpath("input.txt").read_text()


sum_of_all_numbers = 0

for _match in re.finditer(r"-?\d+", input_data):
    sum_of_all_numbers += int(_match.group(0))

print(sum_of_all_numbers)
