from collections import defaultdict
from itertools import pairwise, permutations
from pathlib import Path


input_data = Path(__file__).parent.joinpath("input.txt").read_text()

lines = [line for line in input_data.split("\n") if line]

distances: dict[str, dict[str, int]] = defaultdict(dict)

for line in lines:
    start, _, end, _, distance = line.split()
    distances[start][end] = int(distance)
    distances[end][start] = int(distance)

locations = set(distances.keys())

longest_distance = 0

for permutation in permutations(locations):
    distance = sum(distances[start][end] for start, end in pairwise(permutation))

    longest_distance = max(longest_distance, distance)

print(longest_distance)
