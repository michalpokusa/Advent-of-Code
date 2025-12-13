from pathlib import Path

from advent_of_code import AdventOfCode


DEFAULT_EXAMPLE_INPUT_FILE_PATH = Path(__file__).parent.joinpath("example_input.txt")
DEFAULT_INPUT_FILE_PATH = Path(__file__).parent.joinpath("input.txt")

MEMORY_SPACE_SIZE = 70


class AdventOfCode2024Day18Part1(AdventOfCode):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.falling_bytes_positions = [
            tuple(map(int, line.split(",")))
            for line in self.input_data.split("\n")
            if line
        ]

    def is_inside_memory_space(
        self, memory_space: list[list[str | int]], y: int, x: int
    ) -> bool:
        return 0 <= y < len(memory_space) and 0 <= x < len(memory_space[0])

    def set_corrupted_bytes(
        self, memory_space: list[list[str | int]], locations: list[tuple[int, int]]
    ) -> None:
        for x, y in locations:
            memory_space[y][x] = "#"

    def get_answer(self):
        memory_space = [
            ["." for _ in range(MEMORY_SPACE_SIZE + 1)]
            for _ in range(MEMORY_SPACE_SIZE + 1)
        ]

        self.set_corrupted_bytes(memory_space, self.falling_bytes_positions[:1024])

        top_left_corner = (0, 0)
        positions_to_check = [
            (0, top_left_corner),
        ]

        while positions_to_check:
            steps, (y, x) = positions_to_check.pop(0)

            # Right
            if self.is_inside_memory_space(memory_space, y, x + 1):
                if memory_space[y][x + 1] == ".":
                    memory_space[y][x + 1] = steps + 1
                    positions_to_check.append((steps + 1, (y, x + 1)))

            # Left
            if self.is_inside_memory_space(memory_space, y, x - 1):
                if memory_space[y][x - 1] == ".":
                    memory_space[y][x - 1] = steps + 1
                    positions_to_check.append((steps + 1, (y, x - 1)))

            # Up
            if self.is_inside_memory_space(memory_space, y - 1, x):
                if memory_space[y - 1][x] == ".":
                    memory_space[y - 1][x] = steps + 1
                    positions_to_check.append((steps + 1, (y - 1, x)))

            # Down
            if self.is_inside_memory_space(memory_space, y + 1, x):
                if memory_space[y + 1][x] == ".":
                    memory_space[y + 1][x] = steps + 1
                    positions_to_check.append((steps + 1, (y + 1, x)))

        return memory_space[MEMORY_SPACE_SIZE][MEMORY_SPACE_SIZE]


class AdventOfCode2024Day18Part2(AdventOfCode2024Day18Part1):

    def get_answer(self):
        memory_space = [
            ["." for _ in range(MEMORY_SPACE_SIZE + 1)]
            for _ in range(MEMORY_SPACE_SIZE + 1)
        ]

        top_left_corner = (0, 0)

        self.set_corrupted_bytes(memory_space, self.falling_bytes_positions[:1024])

        for byte_x, byte_y in self.falling_bytes_positions[1024:]:
            for _y in range(MEMORY_SPACE_SIZE + 1):
                for _x in range(MEMORY_SPACE_SIZE + 1):
                    if isinstance(memory_space[_y][_x], int):
                        memory_space[_y][_x] = "."

            memory_space[byte_y][byte_x] = "#"
            memory_space[0][0] = 0

            positions_to_check = [
                (0, top_left_corner),
            ]

            while positions_to_check:
                steps, (y, x) = positions_to_check.pop(0)

                # Right
                if self.is_inside_memory_space(memory_space, y, x + 1):
                    if memory_space[y][x + 1] == ".":
                        memory_space[y][x + 1] = steps + 1
                        positions_to_check.append((steps + 1, (y, x + 1)))

                # Left
                if self.is_inside_memory_space(memory_space, y, x - 1):
                    if memory_space[y][x - 1] == ".":
                        memory_space[y][x - 1] = steps + 1
                        positions_to_check.append((steps + 1, (y, x - 1)))

                # Up
                if self.is_inside_memory_space(memory_space, y - 1, x):
                    if memory_space[y - 1][x] == ".":
                        memory_space[y - 1][x] = steps + 1
                        positions_to_check.append((steps + 1, (y - 1, x)))

                # Down
                if self.is_inside_memory_space(memory_space, y + 1, x):
                    if memory_space[y + 1][x] == ".":
                        memory_space[y + 1][x] = steps + 1
                        positions_to_check.append((steps + 1, (y + 1, x)))

            if memory_space[MEMORY_SPACE_SIZE][MEMORY_SPACE_SIZE] == ".":
                return f"{byte_x},{byte_y}"


if __name__ == "__main__":
    answer = AdventOfCode2024Day18Part2(DEFAULT_INPUT_FILE_PATH).get_answer()
    print(answer)
