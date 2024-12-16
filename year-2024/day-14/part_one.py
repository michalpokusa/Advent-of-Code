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

for robot in robots:
    robot.move(100)

horizontal_half = SPACE_WIDTH // 2
vertical_half = SPACE_HEIGHT // 2

robots_in_top_left_quadrant = sum(
    1
    for robot in robots
    if robot.position_x < horizontal_half and robot.position_y < vertical_half
)
robots_in_top_right_quadrant = sum(
    1
    for robot in robots
    if horizontal_half < robot.position_x < SPACE_WIDTH
    and robot.position_y < vertical_half
)
robots_in_bottom_left_quadrant = sum(
    1
    for robot in robots
    if robot.position_x < horizontal_half
    and vertical_half < robot.position_y < SPACE_HEIGHT
)
robots_in_bottom_right_quadrant = sum(
    1
    for robot in robots
    if horizontal_half < robot.position_x < SPACE_WIDTH
    and vertical_half < robot.position_y < SPACE_HEIGHT
)

safety_factor = (
    robots_in_top_left_quadrant
    * robots_in_top_right_quadrant
    * robots_in_bottom_left_quadrant
    * robots_in_bottom_right_quadrant
)


print(safety_factor)
