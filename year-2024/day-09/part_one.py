from pathlib import Path

input_data = Path(__file__).parent.joinpath("input.txt").read_text().strip()


def expand_disk_map(disk_map: str) -> list:
    disk_map_len = len(disk_map)

    expanded_disk_map = []
    file_index = 0

    for idx in range(0, disk_map_len - 1, 2):
        file_length = int(disk_map[idx])
        free_space_length = int(disk_map[idx + 1])

        expanded_disk_map.extend([file_index] * file_length)
        expanded_disk_map.extend(["."] * free_space_length)

        file_index += 1

    # Last file
    file_length = int(disk_map[-1])
    expanded_disk_map.extend([file_index] * file_length)

    return expanded_disk_map


def compact_filesystem(filesystem: list) -> list:
    compacted_filesystem = [*filesystem]

    for idx in range(len(compacted_filesystem) - 1, 0, -1):
        if compacted_filesystem[idx] == ".":
            continue

        file_id = compacted_filesystem[idx]

        try:
            first_free_space_idx = compacted_filesystem.index(".")
        except ValueError:
            break

        if idx < first_free_space_idx:
            break

        compacted_filesystem[first_free_space_idx] = file_id
        compacted_filesystem[idx] = "."

    return compacted_filesystem


def calculate_checksum(filesystem: list) -> int:
    checksum = 0

    for symbol_idx, symbol in enumerate(filesystem):

        if symbol == ".":
            break

        checksum += symbol_idx * symbol

    return checksum


expanded_disk_map = expand_disk_map(input_data)
compacted_filesystem = compact_filesystem(expanded_disk_map)
checksum = calculate_checksum(compacted_filesystem)

print(checksum)
