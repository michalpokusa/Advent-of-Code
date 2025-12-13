from collections import defaultdict
from itertools import combinations
from pathlib import Path

from advent_of_code import AdventOfCode


DEFAULT_EXAMPLE_INPUT_FILE_PATH = Path(__file__).parent.joinpath("example_input.txt")
DEFAULT_INPUT_FILE_PATH = Path(__file__).parent.joinpath("input.txt")


class AdventOfCode2024Day23Part1(AdventOfCode):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.computer_connections: dict[str, set[str]] = defaultdict(set)
        self.unique_computers: set[str] = set()

        for line in self.input_data.split("\n"):
            if not line:
                continue

            computer1, computer2 = line.split("-")

            self.computer_connections[computer1].add(computer2)
            self.computer_connections[computer2].add(computer1)

            self.unique_computers.add(computer1)
            self.unique_computers.add(computer2)

    def get_answer(self):
        sets_of_three_interconnected_computers: set[str] = set()

        for computers in combinations(self.unique_computers, 3):
            computer1, computer2, computer3 = computers

            # 1 <--> 2
            if computer1 not in self.computer_connections[computer2]:
                continue

            # 1 <--> 3
            if computer1 not in self.computer_connections[computer3]:
                continue

            # 2 <--> 3
            if computer2 not in self.computer_connections[computer3]:
                continue

            sets_of_three_interconnected_computers.add(",".join(sorted(computers)))

        sets_of_computers_that_starts_with_t = set()

        for set_of_computers in sets_of_three_interconnected_computers:
            if any(
                computer.startswith("t") for computer in set_of_computers.split(",")
            ):
                sets_of_computers_that_starts_with_t.add(set_of_computers)

        return len(sets_of_computers_that_starts_with_t)


class AdventOfCode2024Day23Part2(AdventOfCode2024Day23Part1):

    def get_answer(self):
        computer_sets: set[str] = set()

        for computer, connected_computers in self.computer_connections.items():
            for connected_computer in connected_computers:
                computer_sets.add(",".join(sorted({computer, connected_computer})))

        for iter_idx, computer in enumerate(self.unique_computers):
            progress_percent = round(
                (iter_idx + 1) / len(self.unique_computers) * 100, 2
            )
            print(
                f"{progress_percent}%".rjust(6), f"- {len(computer_sets)} computer sets"
            )

            new_computer_sets = set()

            for computer_set in computer_sets:
                computers_in_set = computer_set.split(",")

                if computer in computers_in_set:
                    continue

                is_connected_to_every_other = all(
                    computer in self.computer_connections[computer_in_set]
                    for computer_in_set in computers_in_set
                )

                if is_connected_to_every_other:
                    new_computer_sets.add(
                        ",".join(sorted({computer, *computers_in_set}))
                    )

            computer_sets.update(new_computer_sets)

        largest_computer_set = max(
            computer_sets, key=lambda computer_set: len(computer_set.split(","))
        )

        return largest_computer_set


if __name__ == "__main__":
    answer = AdventOfCode2024Day23Part2(DEFAULT_INPUT_FILE_PATH).get_answer()
    print(answer)
