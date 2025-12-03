import re
from pathlib import Path

input_data = Path(__file__).parent.joinpath("input.txt").read_text().strip()

banks = [list(map(int, line)) for line in input_data.split("\n")]

total_output_joltage = 0


for bank in banks:
    available_joltages = sorted(set(bank), reverse=True)
    first_battery_max_joltage = available_joltages[0]

    if bank.index(first_battery_max_joltage) == len(bank) - 1:
        first_battery_max_joltage = available_joltages[1]

    first_battery_position = bank.index(first_battery_max_joltage)
    second_battery_max_joltage = max(bank[first_battery_position + 1 :])

    total_output_joltage += (
        first_battery_max_joltage * 10
    ) + second_battery_max_joltage

print(total_output_joltage)
