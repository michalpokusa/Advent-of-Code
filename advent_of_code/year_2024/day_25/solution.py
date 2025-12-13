from pathlib import Path

from advent_of_code import AdventOfCode


DEFAULT_EXAMPLE_INPUT_FILE_PATH = Path(__file__).parent.joinpath("example_input.txt")
DEFAULT_INPUT_FILE_PATH = Path(__file__).parent.joinpath("input.txt")


class AdventOfCode2024Day25Part1(AdventOfCode):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.schematics = [
            schematic.strip() for schematic in self.input_data.split("\n\n")
        ]
        self.locks = [
            self.get_pin_heights(schematic)
            for schematic in self.schematics
            if schematic.startswith("#")
        ]
        self.keys = [
            self.get_pin_heights(schematic)
            for schematic in self.schematics
            if schematic.startswith(".")
        ]

    def get_pin_heights(self, schematic: str) -> tuple[int, int, int, int, int]:
        schematic_map = [list(row) for row in schematic.split("\n")]
        pin_heights = [0, 0, 0, 0, 0]

        for column in range(5):
            for row in schematic_map[1:-1]:
                if row[column] == "#":
                    pin_heights[column] += 1

        return tuple(pin_heights)

    def check_key_fits_in_lock(
        self, key: tuple[int, int, int, int, int], lock: tuple[int, int, int, int, int]
    ) -> bool:
        return all(sum(position) <= 5 for position in zip(key, lock))

    def get_answer(self):
        unique_lock_key_pairs = []

        for lock in self.locks:
            for key in self.keys:
                if self.check_key_fits_in_lock(key, lock):
                    unique_lock_key_pairs.append((lock, key))

        return len(unique_lock_key_pairs)


class AdventOfCode2024Day25Part2(AdventOfCode2024Day25Part1):

    def get_answer(self):
        raise NotImplementedError


if __name__ == "__main__":
    answer = AdventOfCode2024Day25Part1(DEFAULT_INPUT_FILE_PATH).get_answer()
    print(answer)
