import re

from collections import defaultdict
from itertools import permutations
from pathlib import Path

input_data = Path(__file__).parent.joinpath("input.txt").read_text().strip()

rules: dict[str, dict[str, int]] = defaultdict(dict)

LINE_PATTERN = re.compile(
    r"(?P<who>\w+) would (?P<change_direction>gain|lose) (?P<change_value>\d+) happiness units by sitting next to (?P<next_to_who>\w+)."
)

for line in input_data.split("\n"):
    _match = re.match(LINE_PATTERN, line)

    who, change_direction, change_value, next_to_who = _match.groups()

    rules[who][next_to_who] = (
        int(change_value) if change_direction == "gain" else -int(change_value)
    )

people = set(rules.keys())

for person in people:
    rules[person]["me"] = 0
    rules["me"][person] = 0

people.add("me")

optimal_seating_arrangement = None
max_total_happiness_change = 0

for seating_arrangement in permutations(people, len(people)):

    total_happiness_change = 0

    for seat_idx, person in enumerate(seating_arrangement):

        left_idx = (seat_idx - 1) % len(seating_arrangement)
        right_idx = (seat_idx + 1) % len(seating_arrangement)

        left_person = seating_arrangement[left_idx]
        right_person = seating_arrangement[right_idx]

        total_happiness_change += rules[person][left_person]
        total_happiness_change += rules[person][right_person]

    if max_total_happiness_change < total_happiness_change:
        max_total_happiness_change = total_happiness_change
        optimal_seating_arrangement = seating_arrangement


print(max_total_happiness_change)
