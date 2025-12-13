from pathlib import Path

from advent_of_code import AdventOfCode


DEFAULT_EXAMPLE_INPUT_FILE_PATH = Path(__file__).parent.joinpath("example_input.txt")
DEFAULT_INPUT_FILE_PATH = Path(__file__).parent.joinpath("input.txt")


class AdventOfCode2024Day20Part1(AdventOfCode):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.racetrack_map = self.racetrack_map_factory()
        self.starting_position = self.get_starting_position(self.racetrack_map)

    def racetrack_map_factory(self) -> list[list[str]]:
        return [list(line) for line in self.input_data.strip().split("\n")]

    def get_starting_position(self, racetrack_map: list[list[str]]) -> tuple[int, int]:
        for y in range(len(racetrack_map)):
            for x in range(len(racetrack_map[y])):
                if racetrack_map[y][x] == "S":
                    return y, x
        raise ValueError("No starting position found")

    def get_picoseconds_to_reach_end(
        self,
        racetrack_map: list[list[str]],
        starting_position: tuple[int, int],
    ) -> int:
        start_y, start_x = starting_position

        positions_to_check = set([(start_y, start_x, 0)])

        while positions_to_check:
            y, x, picoseconds = positions_to_check.pop()

            # Right
            if racetrack_map[y][x + 1] == ".":
                racetrack_map[y][x + 1] = picoseconds + 1
                positions_to_check.add((y, x + 1, picoseconds + 1))

            # Down
            if racetrack_map[y + 1][x] == ".":
                racetrack_map[y + 1][x] = picoseconds + 1
                positions_to_check.add((y + 1, x, picoseconds + 1))

            # Left
            if racetrack_map[y][x - 1] == ".":
                racetrack_map[y][x - 1] = picoseconds + 1
                positions_to_check.add((y, x - 1, picoseconds + 1))

            # Up
            if racetrack_map[y - 1][x] == ".":
                racetrack_map[y - 1][x] = picoseconds + 1
                positions_to_check.add((y - 1, x, picoseconds + 1))

            if "E" in (
                racetrack_map[y][x + 1],
                racetrack_map[y + 1][x],
                racetrack_map[y][x - 1],
                racetrack_map[y - 1][x],
            ):
                return picoseconds + 1

    def get_answer(self):
        no_cheat_picoseconds = self.get_picoseconds_to_reach_end(
            self.racetrack_map, self.starting_position
        )

        cheats_that_save_more_than_100_picoseconds = 0
        racetrack_height = len(self.racetrack_map)
        racetrack_width = len(self.racetrack_map[0])

        iteration_nr = 0
        total_iterations = (racetrack_height - 2) * (racetrack_width - 2)

        for cheat_y in range(1, racetrack_height - 1):
            for cheat_x in range(1, racetrack_width - 1):

                iteration_nr += 1
                print(f"{iteration_nr}/{total_iterations}", end="\r")

                if self.racetrack_map[cheat_y][cheat_x] != "#":
                    continue

                cheated_racetrack_map = self.racetrack_map_factory()
                cheated_racetrack_map[cheat_y][cheat_x] = "."

                cheated_picoseconds = self.get_picoseconds_to_reach_end(
                    cheated_racetrack_map, self.starting_position
                )

                if cheated_picoseconds < no_cheat_picoseconds:
                    saved_picoseconds = no_cheat_picoseconds - cheated_picoseconds

                    if 100 <= saved_picoseconds:
                        cheats_that_save_more_than_100_picoseconds += 1
        print()
        return cheats_that_save_more_than_100_picoseconds


class AdventOfCode2024Day20Part2(AdventOfCode2024Day20Part1):

    def get_answer(self):
        raise NotImplementedError


if __name__ == "__main__":
    answer = AdventOfCode2024Day20Part1(DEFAULT_INPUT_FILE_PATH).get_answer()
    print(answer)
