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


class Reindeer:

    def __init__(self, flying_speed: int, flying_time: int, resting_time: int) -> None:
        self.flying_speed = flying_speed
        self.flying_time = flying_time
        self.resting_time = resting_time

        self.distance = 0
        self._cycle = self._get_cycle()

        self.points = 0

    def _get_cycle(self):
        while True:
            for _ in range(self.flying_time):
                self.distance += self.flying_speed
                yield

            for _ in range(self.resting_time):
                yield

    def progress(self) -> None:
        next(self._cycle)


reindeers: dict[str, Reindeer] = {
    reindeer: Reindeer(*reindeer_specs[reindeer]) for reindeer in reindeer_specs
}

for _ in range(2503):
    for reindeer in reindeers.values():
        reindeer.progress()

    max_distance = max(reindeers.values(), key=lambda r: r.distance).distance

    for reindeer in reindeers.values():
        if reindeer.distance == max_distance:
            reindeer.points += 1

print(max(reinder.points for reinder in reindeers.values()))
