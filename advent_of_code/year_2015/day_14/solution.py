import re
from pathlib import Path

from advent_of_code import AdventOfCode


DEFAULT_EXAMPLE_INPUT_FILE_PATH = Path(__file__).parent.joinpath("example_input.txt")
DEFAULT_INPUT_FILE_PATH = Path(__file__).parent.joinpath("input.txt")


class AdventOfCode2015Day14Part1(AdventOfCode):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        lines = self.input_data.strip().splitlines()
        self.reindeer_specs: dict[str, tuple[int, int, int]] = dict()
        pattern = re.compile(
            r"(?P<reindeer>\w+) can fly (?P<flying_time>\d+) km/s for (?P<seconds>\d+) seconds, but then must rest for (?P<resting_seconds>\d+) seconds."
        )
        for line in lines:
            match = re.match(pattern, line)
            reindeer, flying_time, seconds, resting_seconds = match.groups()

            self.reindeer_specs[reindeer] = (
                int(flying_time),
                int(seconds),
                int(resting_seconds),
            )

    def get_reindeer_distance_after_n_seconds(
        self, seconds: int, speed: int, flying_time: int, resting_time: int
    ):
        cycle_time = flying_time + resting_time
        cycles = seconds // cycle_time
        remaining_seconds = seconds % cycle_time

        return (
            cycles * flying_time * speed + min(remaining_seconds, flying_time) * speed
        )

    def get_answer(self):
        reindeer_distances = {
            reindeer: self.get_reindeer_distance_after_n_seconds(
                2503, *self.reindeer_specs[reindeer]
            )
            for reindeer in self.reindeer_specs
        }
        return max(reindeer_distances.values())


class AdventOfCode2015Day14Part2(AdventOfCode2015Day14Part1):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        class Reindeer:
            def __init__(
                self, flying_speed: int, flying_time: int, resting_time: int
            ) -> None:
                self.flying_speed = flying_speed
                self.flying_time = flying_time
                self.resting_time = resting_time

                self.distance = 0
                self.state = "flying"
                self.state_time_left = self.flying_time

                self.points = 0

            def progress(self) -> None:
                if self.state_time_left == 0:
                    if self.state == "flying":
                        self.state = "resting"
                        self.state_time_left = self.resting_time
                    else:
                        self.state = "flying"
                        self.state_time_left = self.flying_time

                if self.state == "flying":
                    self.distance += self.flying_speed

                self.state_time_left -= 1

        self.reindeers: dict[str, Reindeer] = {
            reindeer: Reindeer(*self.reindeer_specs[reindeer])
            for reindeer in self.reindeer_specs
        }

    def get_answer(self):
        for _ in range(2503):
            for reindeer in self.reindeers.values():
                reindeer.progress()

            max_distance = max(
                self.reindeers.values(), key=lambda r: r.distance
            ).distance

            for reindeer in self.reindeers.values():
                if reindeer.distance == max_distance:
                    reindeer.points += 1

        return max(reindeer.points for reindeer in self.reindeers.values())


if __name__ == "__main__":
    answer = AdventOfCode2015Day14Part2(DEFAULT_INPUT_FILE_PATH).get_answer()
    print(answer)
