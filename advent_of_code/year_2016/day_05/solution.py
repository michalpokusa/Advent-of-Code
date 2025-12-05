from hashlib import md5
from pathlib import Path

from advent_of_code import AdventOfCode


DEFAULT_EXAMPLE_INPUT_FILE_PATH = Path(__file__).parent.joinpath("example_input.txt")
DEFAULT_INPUT_FILE_PATH = Path(__file__).parent.joinpath("input.txt")


class AdventOfCode2016Day5Part1(AdventOfCode):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.door_id = self.input_data.strip()

    def get_door_password(self, door_id: str) -> str:
        password_letters = []
        index = 0

        for _ in range(8):
            while True:
                hash = md5(f"{door_id}{index}".encode()).hexdigest()

                index += 1
                if hash.startswith("00000"):
                    password_letters.append(hash[5])
                    break

        return "".join(password_letters)

    def get_answer(self):
        return self.get_door_password(self.door_id)


class AdventOfCode2016Day5Part2(AdventOfCode2016Day5Part1):

    def get_door_password(self, door_id: str) -> str:
        password = ["_"] * 8
        index = 0

        while "_" in password:
            hash = md5(f"{door_id}{index}".encode()).hexdigest()
            index += 1

            position = int(hash[5], 16)
            character = hash[6]

            if hash.startswith("00000") and position < 8 and password[position] == "_":
                password[position] = character
                print("".join(password))

        return "".join(password)


if __name__ == "__main__":
    answer = AdventOfCode2016Day5Part2(DEFAULT_INPUT_FILE_PATH).get_answer()
    print(answer)
