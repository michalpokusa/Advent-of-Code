import re

from pathlib import Path


input_data = Path(__file__).parent.joinpath("input.txt").read_text()

towel_patterns_data, desired_designs_data = input_data.split("\n\n")

towel_patterns = [pattern for pattern in towel_patterns_data.split(", ")]
desired_designs = [design for design in desired_designs_data.split("\n") if design]

POSSIBLE_DESIGN_PATTERN = re.compile(f"^({'|'.join(towel_patterns)})+$")


possible_designs = 0

for design in desired_designs:
    if re.fullmatch(POSSIBLE_DESIGN_PATTERN, design):
        possible_designs += 1

print(possible_designs)
