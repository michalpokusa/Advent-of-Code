from functools import lru_cache
from pathlib import Path

from advent_of_code import AdventOfCode


DEFAULT_EXAMPLE_INPUT_FILE_PATH = Path(__file__).parent.joinpath("example_input.txt")
DEFAULT_INPUT_FILE_PATH = Path(__file__).parent.joinpath("input.txt")


class AdventOfCode2024Day11Part1(AdventOfCode):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.stones = [int(number) for number in self.input_data.strip().split(" ")]

    def blink(self, stones: list[int]) -> list[int]:
        new_stones = []

        for stone in stones:
            # 1. If the stone is engraved with the number 0,
            #    it is replaced by a stone engraved with the number 1.
            if stone == 0:
                new_stones.append(1)
            # 2. If the stone is engraved with a number that has an even number of digits,
            #    it is replaced by two stones.
            #    The left half of the digits are engraved on the new left stone,
            #    and the right half of the digits are engraved on the new right stone.
            #    (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
            elif len(str(stone)) % 2 == 0:
                half = len(str(stone)) // 2
                new_stones.append(int(str(stone)[:half]))
                new_stones.append(int(str(stone)[half:]))
            # 3. If none of the other rules apply, the stone is replaced by a new stone;
            #    the old stone's number multiplied by 2024 is engraved on the new stone.
            else:
                new_stones.append(stone * 2024)

        return new_stones

    def get_answer(self):
        for _ in range(25):
            self.stones = self.blink(self.stones)

        return len(self.stones)


class AdventOfCode2024Day11Part2(AdventOfCode):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.original_stones = {
            int(number) for number in self.input_data.strip().split(" ")
        }

    def blink(self, stone: int) -> list[int]:
        new_stones = []

        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            half = len(str(stone)) // 2
            new_stones.append(int(str(stone)[:half]))
            new_stones.append(int(str(stone)[half:]))
        else:
            new_stones.append(stone * 2024)

        return new_stones

    @lru_cache(maxsize=100_000)
    def get_number_of_stones_after_n_blinks(self, stone: int, nr_of_blinks: int) -> int:
        if nr_of_blinks == 0:
            return 1

        total_stones_after_number_of_blinks = 0
        new_stones = self.blink(stone)

        for new_stone in new_stones:
            total_stones_after_number_of_blinks += (
                self.get_number_of_stones_after_n_blinks(new_stone, nr_of_blinks - 1)
            )

        return total_stones_after_number_of_blinks

    def get_answer(self):
        blinks = 75

        total_stones_after_number_of_blinks = 0

        for stone in self.original_stones:
            total_stones_after_number_of_blinks += (
                self.get_number_of_stones_after_n_blinks(stone, blinks)
            )

        return total_stones_after_number_of_blinks


if __name__ == "__main__":
    answer = AdventOfCode2024Day11Part2(DEFAULT_INPUT_FILE_PATH).get_answer()
    print(answer)
