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


sum_of_the_2000th_secret_numbers = 0

for initial_buyer_secret_number in initial_buyer_secret_numbers:
    secret_number = initial_buyer_secret_number

    for _ in range(2000):
        secret_number = get_next_secret_number(secret_number)

    sum_of_the_2000th_secret_numbers += secret_number

print(sum_of_the_2000th_secret_numbers)
