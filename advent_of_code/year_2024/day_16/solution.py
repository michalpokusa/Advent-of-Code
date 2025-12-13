from pathlib import Path
from dataclasses import dataclass

from prettytable import PrettyTable

from advent_of_code import AdventOfCode


DEFAULT_EXAMPLE_INPUT_FILE_PATH = Path(__file__).parent.joinpath("example_input.txt")
DEFAULT_INPUT_FILE_PATH = Path(__file__).parent.joinpath("input.txt")


@dataclass
class MazePath:
    direction: str
    steps: list[str]
    cost: int


class AdventOfCode2024Day16Part1(AdventOfCode):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.maze = [list(row) for row in self.input_data.split("\n") if row]

    def get_tile_coords(
        self, maze: list[list[str | int]], tile: str
    ) -> tuple[int, int]:
        for y in range(len(maze)):
            for x in range(len(maze[y])):
                if maze[y][x] == tile:
                    return (y, x)
        raise ValueError(f"'{tile}' tile not found in maze")

    def get_direction_change_cost(self, from_: str, to: str) -> int:
        if from_ == to:
            return 0

        return {
            ("north", "east"): 1000,
            ("north", "south"): 2000,
            ("north", "west"): 1000,
            ("east", "north"): 1000,
            ("east", "south"): 1000,
            ("east", "west"): 2000,
            ("south", "north"): 2000,
            ("south", "east"): 1000,
            ("south", "west"): 1000,
            ("west", "north"): 1000,
            ("west", "east"): 2000,
            ("west", "south"): 1000,
        }[(from_, to)]

    def pretty_print_maze(self, maze: list[list[str | int]]) -> None:
        table = PrettyTable()
        table.header = False
        table.align = "c"

        for row in maze:
            table.add_row(row, divider=True)

        Path(__file__).parent.joinpath("maze.txt").write_text(str(table))

    def get_answer(self):
        maze = [row.copy() for row in self.maze]
        start_tile_coords = self.get_tile_coords(maze, "S")
        end_tile_coords = self.get_tile_coords(maze, "E")

        tiles_to_check = [
            (start_tile_coords, MazePath(direction="east", steps=[], cost=0)),
        ]

        paths_that_lead_to_end: list[MazePath] = []

        while tiles_to_check:
            (tile_y, tile_x), maze_path = tiles_to_check.pop(0)

            right_tile = maze[tile_y][tile_x + 1]
            left_tile = maze[tile_y][tile_x - 1]
            above_tile = maze[tile_y - 1][tile_x]
            below_tile = maze[tile_y + 1][tile_x]

            # Right (not yet visited)
            if isinstance(right_tile, str) and right_tile in ".E":
                new_maze_path = MazePath(
                    direction="east",
                    steps=maze_path.steps.copy() + [(tile_y, tile_x + 1)],
                    cost=maze_path.cost
                    + self.get_direction_change_cost(maze_path.direction, "east")
                    + 1,
                )

                if right_tile == "E":
                    paths_that_lead_to_end.append(new_maze_path)
                else:
                    maze[tile_y][tile_x + 1] = new_maze_path
                    tiles_to_check.append(((tile_y, tile_x + 1), new_maze_path))

            # Left (not yet visited)
            if isinstance(left_tile, str) and left_tile in ".E":
                new_maze_path = MazePath(
                    direction="west",
                    steps=maze_path.steps.copy() + [(tile_y, tile_x - 1)],
                    cost=maze_path.cost
                    + self.get_direction_change_cost(maze_path.direction, "west")
                    + 1,
                )

                if left_tile == "E":
                    paths_that_lead_to_end.append(new_maze_path)
                else:
                    maze[tile_y][tile_x - 1] = new_maze_path
                    tiles_to_check.append(((tile_y, tile_x - 1), new_maze_path))

            # Above (not yet visited)
            if isinstance(above_tile, str) and above_tile in ".E":
                new_maze_path = MazePath(
                    direction="north",
                    steps=maze_path.steps.copy() + [(tile_y - 1, tile_x)],
                    cost=maze_path.cost
                    + self.get_direction_change_cost(maze_path.direction, "north")
                    + 1,
                )

                if above_tile == "E":
                    paths_that_lead_to_end.append(new_maze_path)
                else:
                    maze[tile_y - 1][tile_x] = new_maze_path
                    tiles_to_check.append(((tile_y - 1, tile_x), new_maze_path))

            # Below (not yet visited)
            if isinstance(below_tile, str) and below_tile in ".E":
                new_maze_path = MazePath(
                    direction="south",
                    steps=maze_path.steps.copy() + [(tile_y + 1, tile_x)],
                    cost=maze_path.cost
                    + self.get_direction_change_cost(maze_path.direction, "south")
                    + 1,
                )

                if below_tile == "E":
                    paths_that_lead_to_end.append(new_maze_path)
                else:
                    maze[tile_y + 1][tile_x] = new_maze_path
                    tiles_to_check.append(((tile_y + 1, tile_x), new_maze_path))

            # --------------------------------------------------------------

            # Right (visited)
            if isinstance(right_tile, MazePath):
                old_maze_path = right_tile
                new_maze_path = MazePath(
                    direction="east",
                    steps=maze_path.steps.copy() + [(tile_y, tile_x + 1)],
                    cost=maze_path.cost
                    + self.get_direction_change_cost(maze_path.direction, "east")
                    + 1,
                )

                if new_maze_path.cost < old_maze_path.cost:
                    maze[tile_y][tile_x + 1] = new_maze_path
                    tiles_to_check.append(((tile_y, tile_x + 1), new_maze_path))

            # Left (visited)
            if isinstance(left_tile, MazePath):
                old_maze_path = left_tile
                new_maze_path = MazePath(
                    direction="west",
                    steps=maze_path.steps.copy() + [(tile_y, tile_x - 1)],
                    cost=maze_path.cost
                    + self.get_direction_change_cost(maze_path.direction, "west")
                    + 1,
                )

                if new_maze_path.cost < old_maze_path.cost:
                    maze[tile_y][tile_x - 1] = new_maze_path
                    tiles_to_check.append(((tile_y, tile_x - 1), new_maze_path))

            # Above (visited)
            if isinstance(above_tile, MazePath):
                old_maze_path = above_tile
                new_maze_path = MazePath(
                    direction="north",
                    steps=maze_path.steps.copy() + [(tile_y - 1, tile_x)],
                    cost=maze_path.cost
                    + self.get_direction_change_cost(maze_path.direction, "north")
                    + 1,
                )

                if new_maze_path.cost < old_maze_path.cost:
                    maze[tile_y - 1][tile_x] = new_maze_path
                    tiles_to_check.append(((tile_y - 1, tile_x), new_maze_path))

            # Below (visited)
            if isinstance(below_tile, MazePath):
                old_maze_path = below_tile
                new_maze_path = MazePath(
                    direction="south",
                    steps=maze_path.steps.copy() + [(tile_y + 1, tile_x)],
                    cost=maze_path.cost
                    + self.get_direction_change_cost(maze_path.direction, "south")
                    + 1,
                )

                if new_maze_path.cost < old_maze_path.cost:
                    maze[tile_y + 1][tile_x] = new_maze_path
                    tiles_to_check.append(((tile_y + 1, tile_x), new_maze_path))

        cheapest_path = min(paths_that_lead_to_end, key=lambda path: path.cost)

        return cheapest_path.cost


class AdventOfCode2024Day16Part2(AdventOfCode2024Day16Part1):

    def get_answer(self):
        raise NotImplementedError


if __name__ == "__main__":
    answer = AdventOfCode2024Day16Part1(DEFAULT_INPUT_FILE_PATH).get_answer()
    print(answer)
