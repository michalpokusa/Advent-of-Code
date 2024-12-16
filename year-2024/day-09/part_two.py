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


def get_first_n_length_free_space(
    filesystem: list, n: int, max_idx: int
) -> "int | None":
    idx = 0

    while idx < max_idx:
        if filesystem[idx] != ".":
            idx += 1
            continue

        found_enough_free_space = True
        for next_idx in range(idx + 1, idx + n):
            if max_idx <= next_idx:
                return None

            if filesystem[next_idx] != ".":
                found_enough_free_space = False
                break

        if found_enough_free_space:
            return idx

        idx = next_idx


def compact_filesystem(filesystem: list) -> list:
    compacted_filesystem = [*filesystem]
    max_file_id = max(file_id for file_id in filesystem if file_id != ".")

    for file_id in range(max_file_id, -1, -1):
        file_length = filesystem.count(file_id)

        file_start_idx = compacted_filesystem.index(file_id)

        free_space_idx = get_first_n_length_free_space(
            compacted_filesystem, file_length, file_start_idx
        )

        if free_space_idx is None:
            continue

        if file_start_idx < free_space_idx:
            continue

        for idx in range(file_start_idx, file_start_idx + file_length):
            compacted_filesystem[idx] = "."

        for idx in range(free_space_idx, free_space_idx + file_length):
            compacted_filesystem[idx] = file_id

    return compacted_filesystem


def calculate_checksum(filesystem: list) -> int:
    checksum = 0

    for symbol_idx, symbol in enumerate(filesystem):

        if symbol == ".":
            continue

        checksum += symbol_idx * symbol

    return checksum


expanded_disk_map = expand_disk_map(input_data)
compacted_filesystem = compact_filesystem(expanded_disk_map)
checksum = calculate_checksum(compacted_filesystem)


print(checksum)
