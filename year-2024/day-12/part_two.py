from pathlib import Path

input_data = Path(__file__).parent.joinpath("input.txt").read_text()

farm_map = [list(row.strip()) for row in input_data.split("\n") if row.strip()]


def is_inside_map(map: list[list[str]], y: int, x: int) -> bool:
    return 0 <= y < len(map) and 0 <= x < len(map[0])


def get_region_plots(map: list[list[str]], y: int, x: int) -> set[tuple[int, int]]:
    plant_type = map[y][x]
    plots = {(y, x)}
    visited_plots = {(y, x)}

    def area_expands_here(y: int, x: int):
        return (
            is_inside_map(map, y, x)
            and map[y][x] == plant_type
            and (y, x) not in visited_plots
        )

    while plots:
        y, x = plots.pop()

        # Up
        if area_expands_here(y - 1, x):
            plots.add((y - 1, x))
            visited_plots.add((y - 1, x))

        # Right
        if area_expands_here(y, x + 1):
            plots.add((y, x + 1))
            visited_plots.add((y, x + 1))

        # Down
        if area_expands_here(y + 1, x):
            plots.add((y + 1, x))
            visited_plots.add((y + 1, x))

        # Left
        if area_expands_here(y, x - 1):
            plots.add((y, x - 1))
            visited_plots.add((y, x - 1))

    return visited_plots


def get_region_area(map: list[list[str]], y: int, x: int) -> int:

    return len(get_region_plots(map, y, x))


def get_region_number_of_sides(map: list[list[str]], y: int, x: int) -> int:
    region_plots = get_region_plots(map, y, x)

    region_fences = set()

    for y, x in region_plots:

        # Up
        if (y - 1, x) not in region_plots:
            region_fences.add((y, x, "up"))

        # Right
        if (y, x + 1) not in region_plots:
            region_fences.add((y, x, "right"))

        # Down
        if (y + 1, x) not in region_plots:
            region_fences.add((y, x, "down"))

        # Left
        if (y, x - 1) not in region_plots:
            region_fences.add((y, x, "left"))

    sides = 0

    def remove_connected_fences(
        y: int, x: int, dy: int, dx: int, direction: str
    ) -> None:
        connected_fence = (y + dy, x + dx, direction)
        while connected_fence in region_fences:
            region_fences.remove(connected_fence)
            _y, _x, _direction = connected_fence
            connected_fence = (_y + dy, _x + dx, _direction)

    while region_fences:
        sides += 1

        y, x, direction = region_fences.pop()

        # Up connected fences
        remove_connected_fences(y, x, -1, 0, direction)

        # Right connected fences
        remove_connected_fences(y, x, 0, 1, direction)

        # Down connected fences
        remove_connected_fences(y, x, 1, 0, direction)

        # Left connected fences
        remove_connected_fences(y, x, 0, -1, direction)

    return sides


def mark_region_as_fenced(map: list[list[str]], y: int, x: int) -> None:
    plant_type = map[y][x]
    plots = {(y, x)}

    while plots:
        y, x = plots.pop()

        # Mark as fenced
        map[y][x] = "."

        # Up
        if is_inside_map(map, y - 1, x) and map[y - 1][x] == plant_type:
            plots.add((y - 1, x))

        #  Right
        if is_inside_map(map, y, x - 1) and map[y][x - 1] == plant_type:
            plots.add((y, x - 1))

        # Down
        if is_inside_map(map, y + 1, x) and map[y + 1][x] == plant_type:
            plots.add((y + 1, x))

        # Left
        if is_inside_map(map, y, x + 1) and map[y][x + 1] == plant_type:
            plots.add((y, x + 1))


total_fencing_price = 0

for y in range(len(farm_map)):
    for x in range(len(farm_map[y])):

        if farm_map[y][x] == ".":
            continue

        area = get_region_area(farm_map, y, x)
        number_of_sides = get_region_number_of_sides(farm_map, y, x)

        fencing_price = area * number_of_sides

        total_fencing_price += fencing_price

        mark_region_as_fenced(farm_map, y, x)

print(total_fencing_price)
