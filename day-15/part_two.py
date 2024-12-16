from pathlib import Path

input_data = Path(__file__).parent.joinpath("input.txt").read_text()

warehouse_data, moves_data = input_data.split("\n\n")

warehouse_data = (
    warehouse_data.replace("#", "##")
    .replace("O", "[]")
    .replace(".", "..")
    .replace("@", "@.")
)

warehouse_map = [[cell for cell in row] for row in warehouse_data.split("\n")]

moves = [move for move in moves_data.replace("\n", "")]


class CantMoveException(Exception): ...


class Warehouse:

    def __init__(self, warehouse_map: list[list[str]]) -> None:
        self.map = warehouse_map

        robot_y, robot_x = self._get_robot_position()
        self.robot = Robot(self, robot_y, robot_x)

    def _get_robot_position(self) -> tuple[int, int]:
        for y in range(len(self.map)):
            for x in range(len(self.map[y])):
                if self.map[y][x] == "@":
                    return y, x
        raise ValueError("Robot not found in the warehouse")


class Box:

    def __init__(self, warehouse: Warehouse, y: int, x: int) -> None:
        self.warehouse = warehouse
        self.y = y
        self.x = x

    def move(self, move: str, dry_run: bool = False):

        # >
        if move == ">":
            space_to_right = self.warehouse.map[self.y][self.x + 2]

            if space_to_right == "#":
                raise CantMoveException

            if space_to_right == ".":
                if not dry_run:
                    self.warehouse.map[self.y][self.x] = "."
                    self.warehouse.map[self.y][self.x + 1] = "["
                    self.warehouse.map[self.y][self.x + 2] = "]"
                return

            if space_to_right == "[":
                Box(self.warehouse, self.y, self.x + 2).move(">", dry_run)
                if not dry_run:
                    self.move(">")
                return
        # <
        if move == "<":
            space_to_left = self.warehouse.map[self.y][self.x - 1]

            if space_to_left == "#":
                raise CantMoveException

            if space_to_left == ".":
                if not dry_run:
                    self.warehouse.map[self.y][self.x + 1] = "."
                    self.warehouse.map[self.y][self.x] = "]"
                    self.warehouse.map[self.y][self.x - 1] = "["
                return

            if space_to_left == "]":
                Box(self.warehouse, self.y, self.x - 2).move("<", dry_run)
                if not dry_run:
                    self.move("<")
                return

        # v
        if move == "v":
            if (
                self.warehouse.map[self.y + 1][self.x] == "#"
                or self.warehouse.map[self.y + 1][self.x + 1] == "#"
            ):
                raise CantMoveException

            if (
                self.warehouse.map[self.y + 1][self.x] == "."
                and self.warehouse.map[self.y + 1][self.x + 1] == "."
            ):
                if not dry_run:
                    self.warehouse.map[self.y][self.x] = "."
                    self.warehouse.map[self.y][self.x + 1] = "."
                    self.warehouse.map[self.y + 1][self.x] = "["
                    self.warehouse.map[self.y + 1][self.x + 1] = "]"
                return

            if self.warehouse.map[self.y + 1][self.x] == "[":
                Box(self.warehouse, self.y + 1, self.x).move("v", dry_run)

            if self.warehouse.map[self.y + 1][self.x] == "]":
                Box(self.warehouse, self.y + 1, self.x - 1).move("v", dry_run)

            if self.warehouse.map[self.y + 1][self.x + 1] == "[":
                Box(self.warehouse, self.y + 1, self.x + 1).move("v", dry_run)

            if not dry_run:
                self.move("v")

        # ^
        if move == "^":
            if (
                self.warehouse.map[self.y - 1][self.x] == "#"
                or self.warehouse.map[self.y - 1][self.x + 1] == "#"
            ):
                raise CantMoveException

            if (
                self.warehouse.map[self.y - 1][self.x] == "."
                and self.warehouse.map[self.y - 1][self.x + 1] == "."
            ):
                if not dry_run:
                    self.warehouse.map[self.y][self.x] = "."
                    self.warehouse.map[self.y][self.x + 1] = "."
                    self.warehouse.map[self.y - 1][self.x] = "["
                    self.warehouse.map[self.y - 1][self.x + 1] = "]"
                return

            if self.warehouse.map[self.y - 1][self.x] == "[":
                Box(self.warehouse, self.y - 1, self.x).move("^", dry_run)

            if self.warehouse.map[self.y - 1][self.x] == "]":
                Box(self.warehouse, self.y - 1, self.x - 1).move("^", dry_run)

            if self.warehouse.map[self.y - 1][self.x + 1] == "[":
                Box(self.warehouse, self.y - 1, self.x + 1).move("^", dry_run)

            if not dry_run:
                self.move("^")


class Robot:

    def __init__(self, warehouse: Warehouse, y: int, x: int) -> None:
        self.warehouse = warehouse
        self.y = y
        self.x = x

    def move(self, move: str, dry_run: bool = False):

        # >
        if move == ">":
            space_to_right = self.warehouse.map[self.y][self.x + 1]

            if space_to_right == "#":
                raise CantMoveException

            if space_to_right == ".":
                if not dry_run:
                    self.warehouse.map[self.y][self.x] = "."
                    self.warehouse.map[self.y][self.x + 1] = "@"
                    self.x += 1
                return

            if space_to_right == "[":
                Box(self.warehouse, self.y, self.x + 1).move(">", dry_run)
                if not dry_run:
                    self.move(">")
                return
        # <
        if move == "<":
            space_to_left = self.warehouse.map[self.y][self.x - 1]

            if space_to_left == "#":
                raise CantMoveException

            if space_to_left == ".":
                if not dry_run:
                    self.warehouse.map[self.y][self.x] = "."
                    self.warehouse.map[self.y][self.x - 1] = "@"
                    self.x -= 1
                return

            if space_to_left == "]":
                Box(self.warehouse, self.y, self.x - 2).move("<", dry_run)
                if not dry_run:
                    self.move("<")
                return

        # v
        if move == "v":
            space_below = self.warehouse.map[self.y + 1][self.x]

            if space_below == "#":
                raise CantMoveException

            if space_below == ".":
                if not dry_run:
                    self.warehouse.map[self.y][self.x] = "."
                    self.warehouse.map[self.y + 1][self.x] = "@"
                    self.y += 1
                return

            if space_below == "[":
                Box(self.warehouse, self.y + 1, self.x).move("v", dry_run)
                if not dry_run:
                    self.move("v")
                return

            if space_below == "]":
                Box(self.warehouse, self.y + 1, self.x - 1).move("v", dry_run)
                if not dry_run:
                    self.move("v")
                return

        # ^
        if move == "^":
            space_above = self.warehouse.map[self.y - 1][self.x]

            if space_above == "#":
                raise CantMoveException

            if space_above == ".":
                if not dry_run:
                    self.warehouse.map[self.y][self.x] = "."
                    self.warehouse.map[self.y - 1][self.x] = "@"
                    self.y -= 1
                return

            if space_above == "[":
                Box(self.warehouse, self.y - 1, self.x).move("^", dry_run)
                if not dry_run:
                    self.move("^")
                return

            if space_above == "]":
                Box(self.warehouse, self.y - 1, self.x - 1).move("^", dry_run)
                if not dry_run:
                    self.move("^")
                return


def calculate_boxes_gps_coordinates(warehouse: Warehouse) -> int:
    total_gps_coordinates = 0

    for y in range(len(warehouse.map)):
        for x in range(len(warehouse.map[y])):

            if warehouse.map[y][x] != "[":
                continue

            total_gps_coordinates += 100 * y + x

    return total_gps_coordinates


warehouse = Warehouse(warehouse_map)


for move in moves:
    try:
        warehouse.robot.move(move, dry_run=True)
        warehouse.robot.move(move)
    except CantMoveException:
        pass


print(calculate_boxes_gps_coordinates(warehouse))
