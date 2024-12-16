from collections import defaultdict
from pathlib import Path


input_data = Path(__file__).parent.joinpath("input.txt").read_text()

page_ordering_rules_data, updates_data = input_data.split("\n\n")

page_ordering_rules = [
    [int(number) for number in line.split("|")]
    for line in page_ordering_rules_data.split("\n")
]

page_ordering_rules_dict = defaultdict(list)
for rule in page_ordering_rules:
    page_ordering_rules_dict[rule[0]].append(rule[1])


updates = [
    [int(number) for number in line.split(",")]
    for line in updates_data.split("\n")
    if line
]


def is_correct_update(
    update: "list[int]", page_ordering_rules: "dict[int, list[int]]"
) -> bool:
    for before_number in page_ordering_rules.keys():
        if before_number not in update:
            continue

        for after_number in page_ordering_rules[before_number]:
            if after_number not in update:
                continue

            if update.index(before_number) > update.index(after_number):
                return False

    return True


correct_updates = [
    update for update in updates if is_correct_update(update, page_ordering_rules_dict)
]

sum_of_middle_page_number_of_correct_updates = sum(
    [update[int((len(update) - 1) / 2)] for update in correct_updates]
)

print(sum_of_middle_page_number_of_correct_updates)
