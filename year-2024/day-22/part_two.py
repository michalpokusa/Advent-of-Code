from itertools import product
from pathlib import Path


input_data = Path(__file__).parent.joinpath("input.txt").read_text()

initial_buyer_secret_numbers = [
    int(secret_number) for secret_number in input_data.split("\n") if secret_number
]


def mix(secret_number: int, value: int) -> int:
    return secret_number ^ value


def prune(secret_number: int) -> int:
    return secret_number % 16777216


def get_next_secret_number(secret_number: int) -> int:
    # Calculate the result of multiplying the secret number by 64.
    secret_number_x_64 = secret_number * 64

    # Then, mix this result into the secret number. Finally, prune the secret number.
    secret_number = prune(mix(secret_number, secret_number_x_64))

    # Calculate the result of dividing the secret number by 32. Round the result down to the nearest integer.
    secret_number_div_32 = secret_number // 32

    # Then, mix this result into the secret number. Finally, prune the secret number.
    secret_number = prune(mix(secret_number, secret_number_div_32))

    # Calculate the result of multiplying the secret number by 2048.
    secret_number_x_2048 = secret_number * 2048

    # Then, mix this result into the secret number. Finally, prune the secret number.
    secret_number = prune(mix(secret_number, secret_number_x_2048))

    return secret_number


def get_buyer_price(secret_number: int) -> int:
    return secret_number % 10


def get_possible_best_buyer_sequences():
    changes = range(-9, 10)

    for sequence in product(changes, repeat=4):

        if sum(sequence) < 0 or 9 < sum(sequence):
            continue

        yield sequence


def get_subsequence_index(
    sequence: list | tuple, subsequence: list | tuple
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


buyer_price_history = [[] for _ in range(len(initial_buyer_secret_numbers))]
buyer_price_changes = [[] for _ in range(len(initial_buyer_secret_numbers))]

for buyer_idx, initial_buyer_secret_number in enumerate(initial_buyer_secret_numbers):
    secret_number = initial_buyer_secret_number
    previous_price = get_buyer_price(secret_number)

    buyer_price_history[buyer_idx].append(previous_price)

    for generate_idx in range(2000):
        secret_number = get_next_secret_number(secret_number)
        price = get_buyer_price(secret_number)

        buyer_price_history[buyer_idx].append(price)
        buyer_price_changes[buyer_idx].append(price - previous_price)

        previous_price = price


total_bananas = 0
best_buyer_sequence = None

for possible_best_buyer_sequence in get_possible_best_buyer_sequences():
    bananas = 0

    for buyer_idx, buyer_price_change in enumerate(buyer_price_changes):
        subsequence_idx = get_subsequence_index(
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

print(total_bananas)
print(best_buyer_sequence)
