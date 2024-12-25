import re

from pathlib import Path

input_data = Path(__file__).parent.joinpath("input.txt").read_text().strip()

reindeer_specs: dict[str, tuple[int, int, int]] = dict()

LINE_PATTERN = re.compile(
    r"(?P<reindeer>\w+) can fly (?P<flying_time>\d+) km/s for (?P<seconds>\d+) seconds, but then must rest for (?P<resting_seconds>\d+) seconds."
)

for line in input_data.split("\n"):
    _match = re.match(LINE_PATTERN, line)

    reindeer, flying_time, seconds, resting_seconds = _match.groups()

    reindeer_specs[reindeer] = (int(flying_time), int(seconds), int(resting_seconds))


def get_reindeer_distance_after_n_seconds(
    seconds: int, speed: int, flying_time: int, resting_time: int
):
    cycle_time = flying_time + resting_time
    cycles = seconds // cycle_time
    remaining_seconds = seconds % cycle_time

    return cycles * flying_time * speed + min(remaining_seconds, flying_time) * speed


reindeer_distances = {
    reindeer: get_reindeer_distance_after_n_seconds(2503, *reindeer_specs[reindeer])
    for reindeer in reindeer_specs
}


print(max(reindeer_distances.values()))
