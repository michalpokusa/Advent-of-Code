from itertools import product
from pathlib import Path

from advent_of_code import AdventOfCode


DEFAULT_PART1_EXAMPLE_INPUT_FILE_PATH = Path(__file__).parent.joinpath(
    "part1_example_input.txt"
)
DEFAULT_PART2_EXAMPLE_INPUT_FILE_PATH = Path(__file__).parent.joinpath(
    "part2_example_input.txt"
)
DEFAULT_INPUT_FILE_PATH = Path(__file__).parent.joinpath("input.txt")


class AdventOfCode2024Day22Part1(AdventOfCode):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.initial_buyer_secret_numbers = [
            int(secret_number)
            for secret_number in self.input_data.split("\n")
            if secret_number
        ]

    def mix(self, secret_number: int, value: int) -> int:
        return secret_number ^ value

    def prune(self, secret_number: int) -> int:
        return secret_number % 16777216

    def get_next_secret_number(self, secret_number: int) -> int:
        # Calculate the result of multiplying the secret number by 64.
        secret_number_x_64 = secret_number * 64

        # Then, mix this result into the secret number. Finally, prune the secret number.
        secret_number = self.prune(self.mix(secret_number, secret_number_x_64))

        # Calculate the result of dividing the secret number by 32. Round the result down to the nearest integer.
        secret_number_div_32 = secret_number // 32

        # Then, mix this result into the secret number. Finally, prune the secret number.
        secret_number = self.prune(self.mix(secret_number, secret_number_div_32))

        # Calculate the result of multiplying the secret number by 2048.
        secret_number_x_2048 = secret_number * 2048

        # Then, mix this result into the secret number. Finally, prune the secret number.
        secret_number = self.prune(self.mix(secret_number, secret_number_x_2048))

        return secret_number

    def get_answer(self):
        sum_of_the_2000th_secret_numbers = 0

        for initial_buyer_secret_number in self.initial_buyer_secret_numbers:
            secret_number = initial_buyer_secret_number

            for _ in range(2000):
                secret_number = self.get_next_secret_number(secret_number)

            sum_of_the_2000th_secret_numbers += secret_number

        return sum_of_the_2000th_secret_numbers


class AdventOfCode2024Day22Part2(AdventOfCode2024Day22Part1):

    def get_buyer_price(self, secret_number: int) -> int:
        return secret_number % 10

    def get_possible_best_buyer_sequences(self):
        changes = range(-9, 10)

        for sequence in product(changes, repeat=4):
            if 0 <= sum(sequence) <= 9:
                yield sequence

    def get_subsequence_index(
        self, sequence: list | tuple, subsequence: list | tuple
    ) -> int | None:
        subsequence_length = len(subsequence)

        for idx in range(len(sequence) - subsequence_length + 1):
            if sequence[idx] != subsequence[0]:
                continue
            if sequence[idx + 1] != subsequence[1]:
                continue
            if sequence[idx + 2] != subsequence[2]:
                continue
            if sequence[idx + 3] != subsequence[3]:
                continue

            return idx

        return None

    def get_answer(self):
        buyer_price_history = [
            [] for _ in range(len(self.initial_buyer_secret_numbers))
        ]
        buyer_price_changes = [
            [] for _ in range(len(self.initial_buyer_secret_numbers))
        ]

        for buyer_idx, initial_buyer_secret_number in enumerate(
            self.initial_buyer_secret_numbers
        ):
            secret_number = initial_buyer_secret_number
            previous_price = self.get_buyer_price(secret_number)

            buyer_price_history[buyer_idx].append(previous_price)

            for _ in range(2000):
                secret_number = self.get_next_secret_number(secret_number)
                price = self.get_buyer_price(secret_number)

                buyer_price_history[buyer_idx].append(price)
                buyer_price_changes[buyer_idx].append(price - previous_price)

                previous_price = price

        total_bananas = 0
        best_buyer_sequence = None

        for possible_best_buyer_sequence in self.get_possible_best_buyer_sequences():
            bananas = 0

            for buyer_idx, buyer_price_change in enumerate(buyer_price_changes):
                subsequence_idx = self.get_subsequence_index(
                    buyer_price_change, list(possible_best_buyer_sequence)
                )
                print(
                    f"{total_bananas} {best_buyer_sequence} {possible_best_buyer_sequence}".ljust(
                        100, " "
                    ),
                    end="\r",
                )

                if subsequence_idx is None:
                    continue

                bananas += buyer_price_history[buyer_idx][subsequence_idx + 4]

            if total_bananas < bananas:
                total_bananas = bananas
                best_buyer_sequence = possible_best_buyer_sequence

        return total_bananas


if __name__ == "__main__":
    answer = AdventOfCode2024Day22Part2(DEFAULT_INPUT_FILE_PATH).get_answer()
    print(answer)
