import re
from collections import defaultdict
from itertools import permutations
from pathlib import Path

from advent_of_code import AdventOfCode


DEFAULT_EXAMPLE_INPUT_FILE_PATH = Path(__file__).parent.joinpath("example_input.txt")
DEFAULT_INPUT_FILE_PATH = Path(__file__).parent.joinpath("input.txt")


class AdventOfCode2015Day13Part1(AdventOfCode):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        lines = self.input_data.strip().splitlines()
        self.hapiness_rules: dict[str, dict[str, int]] = defaultdict(dict)
        pattern = re.compile(
            r"(?P<who>\w+) would (?P<change_direction>gain|lose) (?P<change_value>\d+) happiness units by sitting next to (?P<next_to_who>\w+)."
        )
        for line in lines:
            match = re.match(pattern, line)
            who, change_direction, change_value, next_to_who = match.groups()

            self.hapiness_rules[who][next_to_who] = (
                int(change_value) if change_direction == "gain" else -int(change_value)
            )

        self.attendees = set(self.hapiness_rules.keys())

    def get_answer(self):
        max_total_happiness_change = 0

        for seating_arrangement in permutations(self.attendees, len(self.attendees)):
            total_happiness_change = 0

            for seat_idx, person in enumerate(seating_arrangement):

                left_idx = (seat_idx - 1) % len(seating_arrangement)
                right_idx = (seat_idx + 1) % len(seating_arrangement)

                left_person = seating_arrangement[left_idx]
                right_person = seating_arrangement[right_idx]

                total_happiness_change += self.hapiness_rules[person][left_person]
                total_happiness_change += self.hapiness_rules[person][right_person]

            if max_total_happiness_change < total_happiness_change:
                max_total_happiness_change = total_happiness_change

        return max_total_happiness_change


class AdventOfCode2015Day13Part2(AdventOfCode2015Day13Part1):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        for attendee in self.attendees:
            self.hapiness_rules[attendee]["me"] = 0
            self.hapiness_rules["me"][attendee] = 0

        self.attendees.add("me")


if __name__ == "__main__":
    answer = AdventOfCode2015Day13Part2(DEFAULT_INPUT_FILE_PATH).get_answer()
    print(answer)
