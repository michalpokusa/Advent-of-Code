import re

from dataclasses import dataclass
from pathlib import Path

# SPACE_WIDTH = 11
# SPACE_HEIGHT = 7
# input_data = Path(__file__).parent.joinpath("example_input.txt").read_text()

SPACE_WIDTH = 101
SPACE_HEIGHT = 103
input_data = Path(__file__).parent.joinpath("input.txt").read_text()

INPUT_PARSE_PATTERN = re.compile(
    r"p=(?P<position_x>\d+),(?P<position_y>\d+) v=(?P<velocity_x>-?\d+),(?P<velocity_y>-?\d+)"
)


@dataclass
class Robot:
    position_x: int
    position_y: int

    velocity_x: int
    velocity_y: int

    def move(self, seconds: int = 1):
        self.position_x = (self.position_x + self.velocity_x * seconds) % SPACE_WIDTH
        self.position_y = (self.position_y + self.velocity_y * seconds) % SPACE_HEIGHT


robots = [
    Robot(*[int(value) for value in match.groups()])
    for match in INPUT_PARSE_PATTERN.finditer(input_data)
]


def get_space_with_robots(robots: list[Robot]) -> list[list[str]]:
    space = [["." for _ in range(SPACE_WIDTH)] for _ in range(SPACE_HEIGHT)]

    for robot in robots:
        if space[robot.position_y][robot.position_x] == ".":
            space[robot.position_y][robot.position_x] = "1"
        else:
            robots_count = int(space[robot.position_y][robot.position_x])
            space[robot.position_y][robot.position_x] = str(robots_count + 1)

    return space


def get_space_with_any_robots(robots: list[Robot]) -> list[list[str]]:
    space = [["." for _ in range(SPACE_WIDTH)] for _ in range(SPACE_HEIGHT)]

    for robot in robots:
        if space[robot.position_y][robot.position_x] == ".":
            space[robot.position_y][robot.position_x] = "X"

    return space


def write_space_to_file(space: list[list[str]]):
    file = Path(__file__).parent.joinpath("space.txt")

    with file.open("w") as file:
        for row in space:
            file.write("".join(row) + "\n")


def might_contain_christmas_tree_picture(space: list[list[str]]) -> bool:
    for row in space:
        row = "".join(row)

        if "X" * 10 in row:
            return True

    return False


for seconds in range(1, 10000):

    for robot in robots:
        robot.move()

    space = get_space_with_any_robots(robots)

    if might_contain_christmas_tree_picture(space):
        write_space_to_file(space)
        print(seconds)
        break
