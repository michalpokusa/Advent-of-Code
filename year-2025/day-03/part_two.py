import re
from pathlib import Path

input_data = Path(__file__).parent.joinpath("input.txt").read_text().strip()

banks = [list(map(int, line)) for line in input_data.split("\n")]

total_output_joltage = 0

batteries_per_bank = 12


def calculate_bank_voltage(bank: list[int]) -> int:
    bank_voltage = 0
    for battery_idx, battery_voltage in enumerate(reversed(bank)):
        bank_voltage += battery_voltage * (10**battery_idx)
    return bank_voltage


for bank in banks:

    selected_batteries = []
    left_offset = 0

    for right_offset in range(batteries_per_bank - 1, -1, -1):
        max_battery_joltage = max(bank[left_offset : -right_offset or None])
        left_offset = bank.index(max_battery_joltage, left_offset) + 1

        selected_batteries.append(max_battery_joltage)

    total_output_joltage += calculate_bank_voltage(selected_batteries)

print(total_output_joltage)
