from pathlib import Path
from advent_of_code import AdventOfCode


DEFAULT_EXAMPLE_INPUT_FILE_PATH = Path(__file__).parent.joinpath("example_input.txt")
DEFAULT_INPUT_FILE_PATH = Path(__file__).parent.joinpath("input.txt")


class AdventOfCode2025Day3Part1(AdventOfCode):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.banks = [
            list(map(int, line)) for line in self.input_data.strip().split("\n")
        ]

    def get_answer(self):
        total_output_joltage = 0

        for bank in self.banks:
            available_joltages = sorted(set(bank), reverse=True)
            first_battery_max_joltage = available_joltages[0]

            if bank.index(first_battery_max_joltage) == len(bank) - 1:
                first_battery_max_joltage = available_joltages[1]

            first_battery_position = bank.index(first_battery_max_joltage)
            second_battery_max_joltage = max(bank[first_battery_position + 1 :])

            total_output_joltage += (
                first_battery_max_joltage * 10
            ) + second_battery_max_joltage

        return total_output_joltage


class AdventOfCode2025Day3Part2(AdventOfCode2025Day3Part1):

    @staticmethod
    def calculate_battery_bank_voltage(bank: list[int]) -> int:
        bank_voltage = 0
        for battery_idx, battery_voltage in enumerate(reversed(bank)):
            bank_voltage += battery_voltage * (10**battery_idx)
        return bank_voltage

    def get_answer(self):
        total_output_joltage = 0
        batteries_per_bank = 12

        for bank in self.banks:
            selected_batteries = []
            left_offset = 0

            for right_offset in range(batteries_per_bank - 1, -1, -1):
                max_battery_joltage = max(bank[left_offset : -right_offset or None])
                left_offset = bank.index(max_battery_joltage, left_offset) + 1

                selected_batteries.append(max_battery_joltage)

            total_output_joltage += self.calculate_battery_bank_voltage(
                selected_batteries
            )

        return total_output_joltage


if __name__ == "__main__":
    answer = AdventOfCode2025Day3Part2(DEFAULT_INPUT_FILE_PATH).get_answer()
    print(answer)
