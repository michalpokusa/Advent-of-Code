from pathlib import Path
from advent_of_code import AdventOfCode


DEFAULT_EXAMPLE_INPUT_FILE_PATH = Path(__file__).parent.joinpath("example_input.txt")
DEFAULT_INPUT_FILE_PATH = Path(__file__).parent.joinpath("input.txt")


class AdventOfCode2025Day11Part1(AdventOfCode):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.devices_outputs: dict[str, list[str]] = {}
        for line in self.input_data.strip().splitlines():
            name, outputs = line.split(": ", 1)
            self.devices_outputs[name] = outputs.split(" ")

    def recursive_get_next_possible_path(
        self, start: str, end: str, visited: list[str] | None = None
    ):
        visited = visited or []

        for output in self.devices_outputs[start]:

            if output in visited:
                continue

            if output == end:
                yield [*visited, start, output]
                continue

            yield from self.recursive_get_next_possible_path(
                output, end, [*visited, start]
            )

    def get_answer(self):
        paths_leading_you_to_out = 0

        for you_to_out_path in self.recursive_get_next_possible_path("you", "out"):
            paths_leading_you_to_out += 1

        return paths_leading_you_to_out


class AdventOfCode2025Day11Part2(AdventOfCode2025Day11Part1):

    def get_answer(self):
        raise NotImplementedError


if __name__ == "__main__":
    answer = AdventOfCode2025Day11Part2(DEFAULT_INPUT_FILE_PATH).get_answer()
    print(answer)
