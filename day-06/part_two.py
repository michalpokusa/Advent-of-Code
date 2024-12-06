from pathlib import Path

input_file = Path(__file__).parent.joinpath("input.txt")
part_one_output_file = input_file.with_name(input_file.name.replace("input", "output"))
input_data = input_file.read_text()


def get_guard_position(map: list[list[str]]) -> tuple[int, int]:
    for y, row in enumerate(map):
        for x, column in enumerate(row):
            if column in "^>v<":
                return (y, x)


def is_inside_map(map: list[list[str]], y: int, x: int) -> bool:
    return 0 <= y < len(map) and 0 <= x < len(map[0])


def print_map(map: list[list[str]]):
    for row in map:
        print("".join(row))


def get_possible_obstruction_positions(map: list[list[str]]):
    for row in range(len(map)):
        for column in range(len(map[row])):

            if map[row][column] == "X":
                yield (row, column)


part_one_output_map = [
    [char for char in line]
    for line in part_one_output_file.read_text().split("\n")
    if line
]
map = [[char for char in line] for line in input_data.split("\n") if line]


def does_obstruction_make_guard_stuck(
    map: list[list[str]], obstruction_y: int, obstruction_x: int
) -> bool:
    map = [row.copy() for row in map]

    guard_y, guard_x = get_guard_position(map)

    if (guard_y, guard_x) == (obstruction_y, obstruction_x):
        return False

    map[obstruction_y][obstruction_x] = "O"

    guard_patrol_history = []

    while True:
        guard = map[guard_y][guard_x]

        if (guard, guard_y, guard_x) in guard_patrol_history:
            return True

        guard_patrol_history.append((guard, guard_y, guard_x))

        if guard == "^":
            next_y, next_x = guard_y - 1, guard_x
        elif guard == ">":
            next_y, next_x = guard_y, guard_x + 1
        elif guard == "v":
            next_y, next_x = guard_y + 1, guard_x
        elif guard == "<":
            next_y, next_x = guard_y, guard_x - 1

        if not is_inside_map(map, next_y, next_x):
            map[guard_y][guard_x] = "X"
            return False

        if map[next_y][next_x] in "#O":
            if guard == "^":
                map[guard_y][guard_x] = ">"
            elif guard == ">":
                map[guard_y][guard_x] = "v"
            elif guard == "v":
                map[guard_y][guard_x] = "<"
            elif guard == "<":
                map[guard_y][guard_x] = "^"
        else:
            map[guard_y][guard_x] = "X"
            map[next_y][next_x] = guard
            guard_y, guard_x = next_y, next_x


def save_map(map: list[list[str]], output_path: Path):
    with output_path.open("w") as file:
        for row in map:
            file.write("".join(row) + "\n")


guard_stuck_obstruction_positions = 0

for y, x in get_possible_obstruction_positions(part_one_output_map):
    if does_obstruction_make_guard_stuck(map, y, x):
        guard_stuck_obstruction_positions += 1
        print(f"Guard stuck when obstruction on {y=}, {x=}")
    else:
        print(f"Guard NOT stuck when obstruction on {y=}, {x=}")


print(guard_stuck_obstruction_positions)
