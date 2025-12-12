import re
from dataclasses import dataclass
from pathlib import Path

from advent_of_code import AdventOfCode


DEFAULT_EXAMPLE_INPUT_FILE_PATH = Path(__file__).parent.joinpath("example_input.txt")
DEFAULT_INPUT_FILE_PATH = Path(__file__).parent.joinpath("input.txt")

SPACE_WIDTH = 101
SPACE_HEIGHT = 103


@dataclass
class Robot:
    position_x: int
    position_y: int

    velocity_x: int
    velocity_y: int

    def move(self, seconds: int = 1):
        self.position_x = (self.position_x + self.velocity_x * seconds) % SPACE_WIDTH
        self.position_y = (self.position_y + self.velocity_y * seconds) % SPACE_HEIGHT


class AdventOfCode2024Day14Part1(AdventOfCode):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        pattern = re.compile(
            r"p=(?P<position_x>\d+),(?P<position_y>\d+) v=(?P<velocity_x>-?\d+),(?P<velocity_y>-?\d+)"
        )
        self.robots = [
            Robot(*[int(value) for value in match.groups()])
            for match in pattern.finditer(self.input_data)
        ]

    def get_answer(self):

        for robot in self.robots:
            robot.move(100)

        horizontal_half = SPACE_WIDTH // 2
        vertical_half = SPACE_HEIGHT // 2

        robots_in_top_left_quadrant = sum(
            1
            for robot in self.robots
            if robot.position_x < horizontal_half and robot.position_y < vertical_half
        )
        robots_in_top_right_quadrant = sum(
            1
            for robot in self.robots
            if horizontal_half < robot.position_x < SPACE_WIDTH
            and robot.position_y < vertical_half
        )
        robots_in_bottom_left_quadrant = sum(
            1
            for robot in self.robots
            if robot.position_x < horizontal_half
            and vertical_half < robot.position_y < SPACE_HEIGHT
        )
        robots_in_bottom_right_quadrant = sum(
            1
            for robot in self.robots
            if horizontal_half < robot.position_x < SPACE_WIDTH
            and vertical_half < robot.position_y < SPACE_HEIGHT
        )

        safety_factor = (
            robots_in_top_left_quadrant
            * robots_in_top_right_quadrant
            * robots_in_bottom_left_quadrant
            * robots_in_bottom_right_quadrant
        )

        return safety_factor


class AdventOfCode2024Day14Part2(AdventOfCode2024Day14Part1):

    def get_space_with_robots(self, robots: list[Robot]) -> list[list[str]]:
        space = [["." for _ in range(SPACE_WIDTH)] for _ in range(SPACE_HEIGHT)]

        for robot in robots:
            if space[robot.position_y][robot.position_x] == ".":
                space[robot.position_y][robot.position_x] = "1"
            else:
                robots_count = int(space[robot.position_y][robot.position_x])
                space[robot.position_y][robot.position_x] = str(robots_count + 1)

        return space

    def get_space_with_any_robots(self, robots: list[Robot]) -> list[list[str]]:
        space = [["." for _ in range(SPACE_WIDTH)] for _ in range(SPACE_HEIGHT)]

        for robot in robots:
            if space[robot.position_y][robot.position_x] == ".":
                space[robot.position_y][robot.position_x] = "X"

        return space

    def write_space_to_file(self, space: list[list[str]]):
        file = Path(__file__).parent.joinpath("space.txt")

        with file.open("w") as file_handle:
            for row in space:
                file_handle.write("".join(row) + "\n")

    def might_contain_christmas_tree_picture(self, space: list[list[str]]) -> bool:
        for row in space:
            row_string = "".join(row)

            if "X" * 10 in row_string:
                return True

        return False

    def get_answer(self):
        for seconds in range(1, 10000):
            for robot in self.robots:
                robot.move()

            space = self.get_space_with_any_robots(self.robots)
            if self.might_contain_christmas_tree_picture(space):
                self.write_space_to_file(space)
                return seconds


if __name__ == "__main__":
    answer = AdventOfCode2024Day14Part2(DEFAULT_INPUT_FILE_PATH).get_answer()
    print(answer)
