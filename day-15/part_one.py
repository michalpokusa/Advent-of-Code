from pathlib import Path

input_data = Path(__file__).parent.joinpath("input.txt").read_text()

warehouse_data, moves_data = input_data.split("\n\n")


warehouse_map = [[cell for cell in row] for row in warehouse_data.split("\n")]

moves = [move for move in moves_data.replace("\n", "")]


class Warehouse:

    def __init__(self, warehouse_map: list[list[str]]) -> None:
        self.map = warehouse_map
        self.robot_position = self._get_robot_position()

    def _get_robot_position(self) -> tuple[int, int]:
        for y in range(len(self.map)):
            for x in range(len(self.map[y])):
                if self.map[y][x] == "@":
                    return y, x
        raise ValueError("Robot not found in the warehouse map")

    def _get_move_step(self, move: str) -> tuple[int, int]:
        if move == "^":
            return -1, 0
        if move == ">":
            return 0, 1
        if move == "v":
            return 1, 0
        if move == "<":
            return 0, -1

    def move_robot(self, move: str) -> None:
        robot_y, robot_x = self.robot_position
        move_y, move_x = self._get_move_step(move)

        # Rebot would move into wall
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
        while warehouse.map[box_y][box_x] == "O":

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


def calculate_boxes_gps_coordinates(warehouse: Warehouse) -> int:
    total_gps_coordinates = 0

    for y in range(len(warehouse.map)):
        for x in range(len(warehouse.map[y])):

            if warehouse.map[y][x] != "O":
                continue

            total_gps_coordinates += 100 * y + x

    return total_gps_coordinates


warehouse = Warehouse(warehouse_map)

for move in moves:
    print()
    warehouse.move_robot(move)
    print()

print(calculate_boxes_gps_coordinates(warehouse))
