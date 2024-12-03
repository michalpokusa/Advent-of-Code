from pathlib import Path

input_data = Path("./2/input.txt").read_text()

reports = [
    [int(level) for level in line.split(" ")] for line in input_data.split("\n") if line
]

print()


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


def is_report_safe(report: "tuple[int]"):
    return (
        levels_are_all_incrasing(report) or levels_are_all_decreasing(report)
    ) and two_adjacent_levels_differ_by_1_to_3(report)


def reports_after_problem_dampener(report: "tuple[int]"):
    for index in range(len(report)):
        yield [
            level for level_index, level in enumerate(report) if level_index != index
        ]


def is_report_safe_with_problem_dampener(report: "tuple[int]"):
    for report in reports_after_problem_dampener(report):
        if is_report_safe(report):
            return True

    return False


number_of_safe_reports = 0

for report in reports:

    if is_report_safe_with_problem_dampener(report):
        number_of_safe_reports += 1
        continue

print(number_of_safe_reports)
