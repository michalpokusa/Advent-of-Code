from pathlib import Path


input_data = Path(__file__).parent.joinpath("input.txt").read_text()

towel_patterns_data, desired_designs_data = input_data.split("\n\n")

towel_patterns = [pattern for pattern in towel_patterns_data.split(", ")]
desired_designs = [design for design in desired_designs_data.split("\n") if design]

CACHE = {}


def number_of_ways(design: str, towel_patterns: list[str]) -> int:
    if design in CACHE:
        return CACHE[design]

    total_ways = 0

    for pattern in towel_patterns:

        if design == pattern:
            total_ways += 1

        elif design.startswith(pattern):
            total_ways += number_of_ways(design[len(pattern) :], towel_patterns)

    CACHE[design] = total_ways
    return total_ways


total_different_ways = 0

for design in desired_designs:
    total_different_ways += number_of_ways(design, towel_patterns)
    CACHE.clear()

print(total_different_ways)
