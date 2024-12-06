from pathlib import Path

input_file = Path(__file__).parent.joinpath("input.txt")
output_file = input_file.with_name(input_file.name.replace("input", "output"))
input_data = input_file.read_text()

map = [[char for char in line] for line in input_data.split("\n") if line]


def get_guard_position(map: list[list[str]]) -> tuple[int, int]:
    for y, row in enumerate(map):
        for x, column in enumerate(row):
            if column in "^>v<":
                return (y, x)


def is_inside_map(map: list[list[str]], y: int, x: int) -> bool:
    return 0 <= y < len(map) and 0 <= x < len(map[0])


y, x = get_guard_position(map)
while True:
    guard = map[y][x]

    if not is_inside_map(map, y, x):
        break

    if guard == "^":
        next_y, next_x = y - 1, x
    elif guard == ">":
        next_y, next_x = y, x + 1
    elif guard == "v":
        next_y, next_x = y + 1, x
    elif guard == "<":
        next_y, next_x = y, x - 1

    if not is_inside_map(map, next_y, next_x):
        map[y][x] = "X"
        break

    if map[next_y][next_x] == "#":
        if guard == "^":
            map[y][x] = ">"
        elif guard == ">":
            map[y][x] = "v"
        elif guard == "v":
            map[y][x] = "<"
        elif guard == "<":
            map[y][x] = "^"
    else:
        map[y][x] = "X"
        map[next_y][next_x] = guard
        y, x = next_y, next_x


def save_map(map: list[list[str]], output_path: Path):
    with output_path.open("w") as file:
        for row in map:
            file.write("".join(row) + "\n")


visited_positions = sum(row.count("X") for row in map)

print(visited_positions)
save_map(map, output_file)
