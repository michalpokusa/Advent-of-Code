from pathlib import Path

input_data = Path(__file__).parent.joinpath("input.txt").read_text()

reports = [
    [int(level) for level in line.split(" ")] for line in input_data.split("\n") if line
]


def levels_are_all_incrasing(report: "tuple[int]"):
    previous_level = report[0]

    for level in report[1:]:
        if level < previous_level:
            return False

        previous_level = level

    return True


def levels_are_all_decreasing(report: "tuple[int]"):
    previous_level = report[0]

    for level in report[1:]:
        if level > previous_level:
            return False

        previous_level = level

    return True


def two_adjacent_levels_differ_by_1_to_3(report: "tuple[int]"):
    previous_level = report[0]

    for level in report[1:]:
        if not (1 <= abs(level - previous_level) <= 3):
            return False

        previous_level = level

    return True


number_of_safe_reports = 0

for report in reports:

    if (
        levels_are_all_incrasing(report) or levels_are_all_decreasing(report)
    ) and two_adjacent_levels_differ_by_1_to_3(report):
        number_of_safe_reports += 1
        continue

print(number_of_safe_reports)
