from pathlib import Path

from advent_of_code import AdventOfCode


DEFAULT_EXAMPLE_INPUT_FILE_PATH = Path(__file__).parent.joinpath("example_input.txt")
DEFAULT_INPUT_FILE_PATH = Path(__file__).parent.joinpath("input.txt")


class AdventOfCode2024Day2Part1(AdventOfCode):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.reports = [
            [int(level) for level in line.split(" ")]
            for line in self.input_data.split("\n")
            if line
        ]

    def levels_are_all_incrasing(self, report: "tuple[int]"):
        previous_level = report[0]

        for level in report[1:]:
            if level < previous_level:
                return False

            previous_level = level

        return True

    def levels_are_all_decreasing(self, report: "tuple[int]"):
        previous_level = report[0]

        for level in report[1:]:
            if level > previous_level:
                return False

            previous_level = level

        return True

    def two_adjacent_levels_differ_by_1_to_3(self, report: "tuple[int]"):
        previous_level = report[0]

        for level in report[1:]:
            if not (1 <= abs(level - previous_level) <= 3):
                return False

            previous_level = level

        return True

    def get_answer(self):
        number_of_safe_reports = 0

        for report in self.reports:
            if (
                self.levels_are_all_incrasing(report)
                or self.levels_are_all_decreasing(report)
            ) and self.two_adjacent_levels_differ_by_1_to_3(report):
                number_of_safe_reports += 1
                continue

        return number_of_safe_reports


class AdventOfCode2024Day2Part2(AdventOfCode2024Day2Part1):

    def is_report_safe(self, report: "tuple[int]"):
        return (
            self.levels_are_all_incrasing(report)
            or self.levels_are_all_decreasing(report)
        ) and self.two_adjacent_levels_differ_by_1_to_3(report)

    def reports_after_problem_dampener(self, report: "tuple[int]"):
        for index in range(len(report)):
            yield [
                level
                for level_index, level in enumerate(report)
                if level_index != index
            ]

    def is_report_safe_with_problem_dampener(self, report: "tuple[int]"):
        for report_without_level in self.reports_after_problem_dampener(report):
            if self.is_report_safe(report_without_level):
                return True

        return False

    def get_answer(self):
        number_of_safe_reports = 0

        for report in self.reports:
            if self.is_report_safe_with_problem_dampener(report):
                number_of_safe_reports += 1

        return number_of_safe_reports


if __name__ == "__main__":
    answer = AdventOfCode2024Day2Part2(DEFAULT_INPUT_FILE_PATH).get_answer()
    print(answer)
