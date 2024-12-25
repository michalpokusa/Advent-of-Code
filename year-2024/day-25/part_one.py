from pathlib import Path

input_data = Path(__file__).parent.joinpath("input.txt").read_text()

schematics = [schematic.strip() for schematic in input_data.split("\n\n")]


def get_pin_heights(schematic: str) -> tuple[int, int, int, int, int]:

    schematic_map = [list(row) for row in schematic.split("\n")]
    pin_heights = [0, 0, 0, 0, 0]

    for column in range(5):
        for row in schematic_map[1:-1]:
            if row[column] == "#":
                pin_heights[column] += 1

    return tuple(pin_heights)


locks = [
    get_pin_heights(schematic) for schematic in schematics if schematic.startswith("#")
]
keys = [
    get_pin_heights(schematic) for schematic in schematics if schematic.startswith(".")
]


def check_key_fits_in_lock(
    key: tuple[int, int, int, int, int], lock: tuple[int, int, int, int, int]
) -> bool:
    return all(sum(position) <= 5 for position in zip(key, lock))


unique_lock_key_pairs = []

for lock in locks:
    for key in keys:
        if check_key_fits_in_lock(key, lock):
            unique_lock_key_pairs.append((lock, key))

print(len(unique_lock_key_pairs))
