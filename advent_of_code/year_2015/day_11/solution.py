from pathlib import Path

from advent_of_code import AdventOfCode


DEFAULT_EXAMPLE_INPUT_FILE_PATH = Path(__file__).parent.joinpath("example_input.txt")
DEFAULT_INPUT_FILE_PATH = Path(__file__).parent.joinpath("input.txt")


class AdventOfCode2015Day11Part1(AdventOfCode):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.password = self.input_data.strip()

    lowercase_letters = "abcdefghijklmnopqrstuvwxyz"

    # Passwords must include one increasing straight of at least three letters,
    # like abc, bcd, cde, and so on, up to xyz. They cannot skip letters; abd doesn't count.
    # def includes_one
    def password_includes_one_increasing_straight_of_three_letters(
        self, password: str
    ) -> bool:
        for i in range(len(self.lowercase_letters) - 2):
            straight = self.lowercase_letters[i : i + 3]

            if straight in password:
                return True
        return False

    # Passwords may not contain the letters i, o, or l, as these letters can be mistaken for
    # other characters and are therefore confusing.
    def password_includes_any_of(self, password: str, letters: str) -> bool:
        for letter in letters:
            if letter in password:
                return True
        return False

    # Passwords must contain at least two different, non-overlapping pairs of letters,
    #  aa, bb, or zz.
    def password_contains_at_least_2_pairs_of_letters(self, password: str) -> bool:
        pairs_of_letters = 0
        for letter in self.lowercase_letters:
            if letter * 2 in password:
                pairs_of_letters += 1

            if pairs_of_letters >= 2:
                return True
        return False

    def password_meets_requirements(self, password: str) -> bool:
        if not self.password_includes_one_increasing_straight_of_three_letters(
            password
        ):
            return False

        if self.password_includes_any_of(password, "iol"):
            return False

        if not self.password_contains_at_least_2_pairs_of_letters(password):
            return False

        return True

    def next_potential_password(self, password: str) -> str:
        number = 0
        for power, letter in enumerate(reversed(password)):
            number += self.lowercase_letters.index(letter) * (26**power)

        number += 1

        password = ""
        while number > 0:
            number, remainder = divmod(number, 26)
            password = self.lowercase_letters[remainder] + password

        return password

    def next_password(self, password: str) -> str:
        potential_password = self.next_potential_password(password)

        while not self.password_meets_requirements(potential_password):
            potential_password = self.next_potential_password(potential_password)

        return potential_password

    def get_answer(self):
        return self.next_password(self.password)


class AdventOfCode2015Day11Part2(AdventOfCode2015Day11Part1):

    def get_answer(self):
        password = self.next_password(self.password)

        return self.next_password(password)


if __name__ == "__main__":
    answer = AdventOfCode2015Day11Part2(DEFAULT_INPUT_FILE_PATH).get_answer()
    print(answer)
