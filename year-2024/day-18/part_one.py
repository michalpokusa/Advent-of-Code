from pathlib import Path

input_data = Path(__file__).parent.joinpath("input.txt").read_text()

falling_bytes_positions = [
    (int(line.split(",")[0]), int(line.split(",")[1]))
    for line in input_data.split("\n")
    if line
]

MEMORY_SPACE_SIZE = 70

memory_space = [
    ["." for _ in range(MEMORY_SPACE_SIZE + 1)] for _ in range(MEMORY_SPACE_SIZE + 1)
]


def is_inside_memory_space(memory_space: list[list[str | int]], y: int, x: int) -> bool:
    return 0 <= y < len(memory_space) and 0 <= x < len(memory_space[0])


def set_corrupted_bytes(
    memory_space: list[list[str | int]], locations: list[tuple[int, int]]
) -> None:
    for x, y in locations:
        memory_space[y][x] = "#"


set_corrupted_bytes(memory_space, falling_bytes_positions[:1024])

top_left_corner = (0, 0)
bottom_right_corner = (MEMORY_SPACE_SIZE, MEMORY_SPACE_SIZE)


positions_to_check = [
    (0, top_left_corner),
]

while positions_to_check:
    steps, (y, x) = positions_to_check.pop(0)

    # Right
    if is_inside_memory_space(memory_space, y, x + 1):
        if memory_space[y][x + 1] == ".":
            memory_space[y][x + 1] = steps + 1
            positions_to_check.append((steps + 1, (y, x + 1)))

    # Left
    if is_inside_memory_space(memory_space, y, x - 1):
        if memory_space[y][x - 1] == ".":
            memory_space[y][x - 1] = steps + 1
            positions_to_check.append((steps + 1, (y, x - 1)))

    # Up
    if is_inside_memory_space(memory_space, y - 1, x):
        if memory_space[y - 1][x] == ".":
            memory_space[y - 1][x] = steps + 1
            positions_to_check.append((steps + 1, (y - 1, x)))

    # Down
    if is_inside_memory_space(memory_space, y + 1, x):
        if memory_space[y + 1][x] == ".":
            memory_space[y + 1][x] = steps + 1
            positions_to_check.append((steps + 1, (y + 1, x)))

print(memory_space[MEMORY_SPACE_SIZE][MEMORY_SPACE_SIZE])
