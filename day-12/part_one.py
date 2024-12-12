from pathlib import Path

input_data = Path(__file__).parent.joinpath("input.txt").read_text()

farm_map = [list(row.strip()) for row in input_data.split("\n") if row.strip()]


def is_inside_map(map: list[list[str]], y: int, x: int) -> bool:
    return 0 <= y < len(map) and 0 <= x < len(map[0])


def get_region_area(map: list[list[str]], y: int, x: int) -> int:
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

    return len(visited_plots)


def get_region_perimeter(map: list[list[str]], y: int, x: int) -> int:
    plant_type = map[y][x]
    plots = {(y, x)}
    visited_plots = {(y, x)}

    def area_expands_here(y: int, x: int):
        return (
            is_inside_map(map, y, x)
            and map[y][x] == plant_type
            and (y, x) not in visited_plots
        )

    fences = 0

    while plots:
        y, x = plots.pop()

        # Up
        if area_expands_here(y - 1, x):
            plots.add((y - 1, x))
            visited_plots.add((y - 1, x))
        else:
            if (y - 1, x) not in visited_plots:
                fences += 1

        # Right
        if area_expands_here(y, x + 1):
            plots.add((y, x + 1))
            visited_plots.add((y, x + 1))
        else:
            if (y, x + 1) not in visited_plots:
                fences += 1

        # Down
        if area_expands_here(y + 1, x):
            plots.add((y + 1, x))
            visited_plots.add((y + 1, x))
        else:
            if (y + 1, x) not in visited_plots:
                fences += 1

        # Left
        if area_expands_here(y, x - 1):
            plots.add((y, x - 1))
            visited_plots.add((y, x - 1))
        else:
            if (y, x - 1) not in visited_plots:
                fences += 1

    return fences


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
        if is_inside_map(map, y, x + 1) and map[y][x + 1] == plant_type:
            plots.add((y, x + 1))

        # Down
        if is_inside_map(map, y + 1, x) and map[y + 1][x] == plant_type:
            plots.add((y + 1, x))

        # Left
        if is_inside_map(map, y, x - 1) and map[y][x - 1] == plant_type:
            plots.add((y, x - 1))


total_fencing_price = 0

for y in range(len(farm_map)):
    for x in range(len(farm_map[y])):

        if farm_map[y][x] == ".":
            continue

        area = get_region_area(farm_map, y, x)
        perimeter = get_region_perimeter(farm_map, y, x)

        fencing_price = area * perimeter

        total_fencing_price += fencing_price

        mark_region_as_fenced(farm_map, y, x)

print(total_fencing_price)
