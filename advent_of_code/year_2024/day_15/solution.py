from pathlib import Path

from advent_of_code import AdventOfCode


DEFAULT_EXAMPLE_INPUT_FILE_PATH = Path(__file__).parent.joinpath("example_input.txt")
DEFAULT_INPUT_FILE_PATH = Path(__file__).parent.joinpath("input.txt")


class Warehouse:

    def __init__(self, warehouse_map: list[list[str]]) -> None:
        self.map = warehouse_map
        self.robot_position = self.get_robot_position()

    def get_robot_position(self) -> tuple[int, int]:
        for y in range(len(self.map)):
            for x in range(len(self.map[y])):
                if self.map[y][x] == "@":
                    return y, x
        raise ValueError("Robot not found in the warehouse map")

    def get_move_step(self, move: str) -> tuple[int, int]:
        if move == "^":
            return -1, 0
        if move == ">":
            return 0, 1
        if move == "v":
            return 1, 0
        if move == "<":
            return 0, -1
        raise ValueError(f"Unknown move: {move}")

    def move_robot(self, move: str) -> None:
        robot_y, robot_x = self.robot_position
        move_y, move_x = self.get_move_step(move)

        # Robot would move into wall
        if self.map[robot_y + move_y][robot_x + move_x] == "#":
            return

        # Robot moves to empty space
        if self.map[robot_y + move_y][robot_x + move_x] == ".":
            self.map[robot_y][robot_x] = "."
            self.map[robot_y + move_y][robot_x + move_x] = "@"
            self.robot_position = robot_y + move_y, robot_x + move_x
            return

        # Robot tries to move a box
        box_y, box_x = robot_y + move_y, robot_x + move_x
        while self.map[box_y][box_x] == "O":

            # Box would move into wall
            if self.map[box_y + move_y][box_x + move_x] == "#":
                return

            # Box would move into another box
            if self.map[box_y + move_y][box_x + move_x] == "O":
                box_y += move_y
                box_x += move_x
                continue

            # Box moves to empty space
            if self.map[box_y + move_y][box_x + move_x] == ".":
                self.map[robot_y][robot_x] = "."
                self.map[robot_y + move_y][robot_x + move_x] = "@"
                self.robot_position = robot_y + move_y, robot_x + move_x
                self.map[box_y + move_y][box_x + move_x] = "O"
                return

    def calculate_boxes_gps_coordinates(self) -> int:
        total_gps_coordinates = 0

        for y in range(len(self.map)):
            for x in range(len(self.map[y])):
                if self.map[y][x] != "O":
                    continue

                total_gps_coordinates += 100 * y + x

        return total_gps_coordinates


class AdventOfCode2024Day15Part1(AdventOfCode):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        warehouse_part, moves_part = self.input_data.split("\n\n")

        self.warehouse_map = [
            [cell for cell in row] for row in warehouse_part.split("\n")
        ]
        self.moves = [move for move in moves_part.replace("\n", "")]

    def get_answer(self):
        warehouse = Warehouse([row.copy() for row in self.warehouse_map])

        for move in self.moves:
            warehouse.move_robot(move)

        return warehouse.calculate_boxes_gps_coordinates()


class CantMoveException(Exception): ...


class SecondWarehouse:

    def __init__(self, warehouse_map: list[list[str]]) -> None:
        self.map = warehouse_map

        robot_y, robot_x = self.get_robot_position()
        self.robot = Robot(self, robot_y, robot_x)

    def get_robot_position(self) -> tuple[int, int]:
        for y in range(len(self.map)):
            for x in range(len(self.map[y])):
                if self.map[y][x] == "@":
                    return y, x
        raise ValueError("Robot not found in the warehouse")


class Box:

    def __init__(self, warehouse: SecondWarehouse, y: int, x: int) -> None:
        self.warehouse = warehouse
        self.y = y
        self.x = x

    def move(self, move: str, dry_run: bool = False):
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

    def __init__(self, warehouse: SecondWarehouse, y: int, x: int) -> None:
        self.warehouse = warehouse
        self.y = y
        self.x = x

    def move(self, move: str, dry_run: bool = False):
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


class AdventOfCode2024Day15Part2(AdventOfCode2024Day15Part1):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        warehouse_part, moves_part = self.input_data.split("\n\n")

        warehouse_part = (
            warehouse_part.replace("#", "##")
            .replace("O", "[]")
            .replace(".", "..")
            .replace("@", "@.")
        )

        self.warehouse_map = [
            [cell for cell in row] for row in warehouse_part.split("\n")
        ]
        self.moves = [move for move in moves_part.replace("\n", "")]

    def calculate_boxes_gps_coordinates(self, warehouse: SecondWarehouse) -> int:
        total_gps_coordinates = 0

        for y in range(len(warehouse.map)):
            for x in range(len(warehouse.map[y])):
                if warehouse.map[y][x] != "[":
                    continue

                total_gps_coordinates += 100 * y + x

        return total_gps_coordinates

    def get_answer(self):
        warehouse = SecondWarehouse([row.copy() for row in self.warehouse_map])

        for move in self.moves:
            try:
                warehouse.robot.move(move, dry_run=True)
                warehouse.robot.move(move)
            except CantMoveException:
                continue

        return self.calculate_boxes_gps_coordinates(warehouse)


if __name__ == "__main__":
    answer = AdventOfCode2024Day15Part2(DEFAULT_INPUT_FILE_PATH).get_answer()
    print(answer)
