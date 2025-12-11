from pathlib import Path

from advent_of_code import AdventOfCode


DEFAULT_EXAMPLE_INPUT_FILE_PATH = Path(__file__).parent.joinpath("example_input.txt")
DEFAULT_INPUT_FILE_PATH = Path(__file__).parent.joinpath("input.txt")


class AdventOfCode2024Day6Part1(AdventOfCode):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.map = [
            [char for char in line] for line in self.input_data.split("\n") if line
        ]

    def get_guard_position(self, map: list[list[str]]) -> tuple[int, int]:
        for y, row in enumerate(map):
            for x, column in enumerate(row):
                if column in "^>v<":
                    return (y, x)

    def is_inside_map(self, map: list[list[str]], y: int, x: int) -> bool:
        return 0 <= y < len(map) and 0 <= x < len(map[0])

    def simulate_guard_patrol(self, map: list[list[str]]) -> list[list[str]]:
        map_copy = [row.copy() for row in map]

        y, x = self.get_guard_position(map_copy)

        while True:
            guard = map_copy[y][x]

            if guard == "^":
                next_y, next_x = y - 1, x
            elif guard == ">":
                next_y, next_x = y, x + 1
            elif guard == "v":
                next_y, next_x = y + 1, x
            elif guard == "<":
                next_y, next_x = y, x - 1
            else:
                raise ValueError(f"Unknown guard direction: {guard}")

            if not self.is_inside_map(map_copy, next_y, next_x):
                map_copy[y][x] = "X"
                break

            if map_copy[next_y][next_x] == "#":
                if guard == "^":
                    map_copy[y][x] = ">"
                elif guard == ">":
                    map_copy[y][x] = "v"
                elif guard == "v":
                    map_copy[y][x] = "<"
                elif guard == "<":
                    map_copy[y][x] = "^"
            else:
                map_copy[y][x] = "X"
                map_copy[next_y][next_x] = guard
                y, x = next_y, next_x

        return map_copy

    def print_map(self, map: list[list[str]]):
        for row in map:
            print("".join(row))

    def get_answer(self):
        map = self.simulate_guard_patrol(self.map)
        self.print_map(map)
        visited_positions = sum(row.count("X") for row in map)
        return visited_positions


class AdventOfCode2024Day6Part2(AdventOfCode2024Day6Part1):

    def get_possible_obstruction_positions(self, map: list[list[str]]):
        for row in range(len(map)):
            for column in range(len(map[row])):

                if map[row][column] == "X":
                    yield (row, column)

    def does_obstruction_make_guard_stuck(
        self, map: list[list[str]], obstruction_y: int, obstruction_x: int
    ) -> bool:
        map_copy = [row.copy() for row in map]

        guard_y, guard_x = self.get_guard_position(map_copy)

        if (guard_y, guard_x) == (obstruction_y, obstruction_x):
            return False

        map_copy[obstruction_y][obstruction_x] = "O"

        guard_patrol_history = set()

        while True:
            guard = map_copy[guard_y][guard_x]

            if (guard, guard_y, guard_x) in guard_patrol_history:
                return True

            guard_patrol_history.add((guard, guard_y, guard_x))

            if guard == "^":
                next_y, next_x = guard_y - 1, guard_x
            elif guard == ">":
                next_y, next_x = guard_y, guard_x + 1
            elif guard == "v":
                next_y, next_x = guard_y + 1, guard_x
            elif guard == "<":
                next_y, next_x = guard_y, guard_x - 1
            else:
                raise ValueError(f"Unknown guard direction: {guard}")

            if not self.is_inside_map(map_copy, next_y, next_x):
                map_copy[guard_y][guard_x] = "X"
                return False

            if map_copy[next_y][next_x] in "#O":
                if guard == "^":
                    map_copy[guard_y][guard_x] = ">"
                elif guard == ">":
                    map_copy[guard_y][guard_x] = "v"
                elif guard == "v":
                    map_copy[guard_y][guard_x] = "<"
                elif guard == "<":
                    map_copy[guard_y][guard_x] = "^"
            else:
                map_copy[guard_y][guard_x] = "X"
                map_copy[next_y][next_x] = guard
                guard_y, guard_x = next_y, next_x

    def get_answer(self):
        map_after_patrol_without_obstructions = self.simulate_guard_patrol(self.map)
        guard_stuck_obstruction_positions = 0

        for y, x in self.get_possible_obstruction_positions(
            map_after_patrol_without_obstructions
        ):
            if self.does_obstruction_make_guard_stuck(self.map, y, x):
                guard_stuck_obstruction_positions += 1

        return guard_stuck_obstruction_positions


if __name__ == "__main__":
    answer = AdventOfCode2024Day6Part2(DEFAULT_INPUT_FILE_PATH).get_answer()
    print(answer)
