import re
from collections import defaultdict
from pathlib import Path

from advent_of_code import AdventOfCode


DEFAULT_EXAMPLE_INPUT_FILE_PATH = Path(__file__).parent.joinpath("example_input.txt")
DEFAULT_INPUT_FILE_PATH = Path(__file__).parent.joinpath("input.txt")


class AdventOfCode2016Day4Part1(AdventOfCode):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.rooms = re.findall(
            r"^([\w-]+)-(\d+)\[(\w+)\]$", self.input_data.strip(), re.MULTILINE
        )

    def get_room_name_checksum(self, encrypted_room_name: str) -> str:
        letters_count = defaultdict(int)

        for letter in encrypted_room_name:
            if letter != "-":
                letters_count[letter] += 1

        sorted_letter_counts = sorted(
            letters_count.items(), key=lambda item: (-item[1], item[0])
        )

        return "".join(letter for letter, count in sorted_letter_counts)[:5]

    def get_answer(self):
        sum_of_sector_ids = 0

        for encrypted_room_name, sector_id, checksum in self.rooms:
            if self.get_room_name_checksum(encrypted_room_name) == checksum:
                sum_of_sector_ids += int(sector_id)

        return sum_of_sector_ids


class AdventOfCode2016Day4Part2(AdventOfCode2016Day4Part1):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.real_rooms = [
            (encrypted_room_name, sector_id, checksum)
            for encrypted_room_name, sector_id, checksum in self.rooms
            if self.get_room_name_checksum(encrypted_room_name) == checksum
        ]

    def decrypt_room_name(self, encrypted_room_name: str, sector_id: int) -> str:
        alphabet = "abcdefghijklmnopqrstuvwxyz"

        decryption_map = {
            letter: alphabet[(index + sector_id) % len(alphabet)]
            for index, letter in enumerate(alphabet)
        }
        decryption_map["-"] = " "

        return "".join(decryption_map[letter] for letter in encrypted_room_name)

    def get_answer(self):
        decrypted_room_names = [
            (
                self.decrypt_room_name(encrypted_room_name, int(sector_id)),
                sector_id,
            )
            for encrypted_room_name, sector_id, checksum in self.real_rooms
        ]

        for decrypted_room_name, sector_id in decrypted_room_names:
            lookup_words = ["north", "pole"]

            if all(word in decrypted_room_name for word in lookup_words):
                return int(sector_id)


if __name__ == "__main__":
    answer = AdventOfCode2016Day4Part2(DEFAULT_INPUT_FILE_PATH).get_answer()
    print(answer)
