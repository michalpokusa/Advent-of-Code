from collections import defaultdict
from pathlib import Path

input_data = Path(__file__).parent.joinpath("input.txt").read_text()

computer_connections: dict[str, set[str]] = defaultdict(set)
unique_computers: set[str] = set()

for line in input_data.split("\n"):
    if not line:
        continue

    computer1, computer2 = line.split("-")

    computer_connections[computer1].add(computer2)
    computer_connections[computer2].add(computer1)

    unique_computers.add(computer1)
    unique_computers.add(computer2)


computer_sets: set[str] = set()


for computer, connected_computers in computer_connections.items():
    for connected_computer in connected_computers:
        computer_sets.add(",".join(sorted({computer, connected_computer})))


for iter_idx, computer in enumerate(unique_computers):
    progress_percent = round((iter_idx + 1) / len(unique_computers) * 100, 2)
    print(f"{progress_percent}%".rjust(6), f"- {len(computer_sets)} computer sets")

    new_computer_sets = set()

    for computer_set in computer_sets:
        computers_in_set = computer_set.split(",")

        if computer in computers_in_set:
            continue

        is_connected_to_every_other = all(
            computer in computer_connections[computer_in_set]
            for computer_in_set in computers_in_set
        )

        if is_connected_to_every_other:
            new_computer_sets.add(",".join(sorted({computer, *computers_in_set})))

    computer_sets.update(new_computer_sets)


largest_computer_set = max(
    computer_sets, key=lambda computer_set: len(computer_set.split(","))
)

print(largest_computer_set)
