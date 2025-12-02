import re
from pathlib import Path

input_data = Path(__file__).parent.joinpath("input.txt").read_text().strip()

id_ranges = [id_range.split("-") for id_range in input_data.split(",")]


def is_id_valid(id: str) -> bool:
    return re.fullmatch(r"^(\d+)\1+$", id) is None


invalid_ids = (
    id
    for first_id, last_id in id_ranges
    for id in range(int(first_id), int(last_id) + 1)
    if not is_id_valid(str(id))
)

print(sum(map(int, invalid_ids)))
