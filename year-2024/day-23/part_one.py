from collections import defaultdict
from itertools import combinations
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

sets_of_three_interconnected_computers: set[str] = set()


for computers in combinations(unique_computers, 3):

    computer1, computer2, computer3 = computers

    # 1 <--> 2
    if computer1 not in computer_connections[computer2]:
        continue

    # 1 <--> 3
    if computer1 not in computer_connections[computer3]:
        continue

    # 2 <--> 3
    if computer2 not in computer_connections[computer3]:
        continue

    sets_of_three_interconnected_computers.add(",".join(sorted(computers)))

sets_of_computers_that_starts_with_t = set()

for set_of_computers in sets_of_three_interconnected_computers:
    if any(computer.startswith("t") for computer in set_of_computers.split(",")):
        sets_of_computers_that_starts_with_t.add(set_of_computers)

print(len(sets_of_computers_that_starts_with_t))
