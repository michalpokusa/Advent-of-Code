from collections import defaultdict
from pathlib import Path

from advent_of_code import AdventOfCode


DEFAULT_EXAMPLE_INPUT_FILE_PATH = Path(__file__).parent.joinpath("example_input.txt")
DEFAULT_INPUT_FILE_PATH = Path(__file__).parent.joinpath("input.txt")


class AdventOfCode2024Day5Part1(AdventOfCode):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        page_ordering_rules_data, updates_data = self.input_data.split("\n\n")

        page_ordering_rules = [
            [int(number) for number in line.split("|")]
            for line in page_ordering_rules_data.split("\n")
        ]

        self.page_ordering_rules_dict = defaultdict(list)
        for rule in page_ordering_rules:
            self.page_ordering_rules_dict[rule[0]].append(rule[1])

        self.updates = [
            [int(number) for number in line.split(",")]
            for line in updates_data.split("\n")
            if line
        ]

    def is_correct_update(
        self, update: "list[int]", page_ordering_rules: "dict[int, list[int]]"
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

    def get_answer(self):
        correct_updates = [
            update
            for update in self.updates
            if self.is_correct_update(update, self.page_ordering_rules_dict)
        ]

        sum_of_middle_page_number_of_correct_updates = sum(
            [update[int((len(update) - 1) / 2)] for update in correct_updates]
        )

        return sum_of_middle_page_number_of_correct_updates


class AdventOfCode2024Day5Part2(AdventOfCode2024Day5Part1):

    def is_correct_update(
        self, update: "list[int]", page_ordering_rules: "dict[int, list[int]]"
    ):
        for before_number in page_ordering_rules.keys():
            if before_number not in update:
                continue

            for after_number in page_ordering_rules[before_number]:
                if after_number not in update:
                    continue

                if update.index(before_number) > update.index(after_number):
                    return False, (before_number, after_number)

        return True, None

    def correct_update(
        self, update: "list[int]", page_ordering_rules: "dict[int, list[int]]"
    ) -> "list[int]":

        while True:
            is_correct, incorrect_pair = self.is_correct_update(
                update, page_ordering_rules
            )

            if is_correct is True:
                return update

            assert incorrect_pair is not None

            before_number, after_number = incorrect_pair

            update.pop(update.index(before_number))
            update.insert(update.index(after_number), before_number)

    def get_answer(self):
        incorrect_updates = [
            update
            for update in self.updates
            if not self.is_correct_update(update, self.page_ordering_rules_dict)[0]
        ]

        corrected_updates = [
            self.correct_update(update, self.page_ordering_rules_dict)
            for update in incorrect_updates
        ]

        sum_of_middle_page_number_of_corrected_updates = sum(
            [update[int((len(update) - 1) / 2)] for update in corrected_updates]
        )

        return sum_of_middle_page_number_of_corrected_updates


if __name__ == "__main__":
    answer = AdventOfCode2024Day5Part2(DEFAULT_INPUT_FILE_PATH).get_answer()
    print(answer)
