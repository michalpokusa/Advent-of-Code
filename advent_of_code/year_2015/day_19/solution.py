import re
from collections import defaultdict
from pathlib import Path

from advent_of_code import AdventOfCode


DEFAULT_EXAMPLE_INPUT_FILE_PATH = Path(__file__).parent.joinpath("example_input.txt")
DEFAULT_INPUT_FILE_PATH = Path(__file__).parent.joinpath("input.txt")


class AdventOfCode2015Day19Part1(AdventOfCode):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        replacements_part, starting_part = self.input_data.strip().split("\n\n")

        self.replacements: dict[str, list[str]] = defaultdict(list)
        for atom, replacement in re.findall(r"(\w+) => (\w+)", replacements_part):
            self.replacements[atom].append(replacement)

        self.medicine_molecule = starting_part.strip()

    def get_answer(self):
        replaceable_parts = [
            (match.group(), match.start(), match.end())
            for match in re.finditer(
                r"|".join(self.replacements.keys()), self.medicine_molecule
            )
        ]

        distinct_molecules = set()

        for part, start, end in replaceable_parts:
            for replacement in self.replacements[part]:
                distinct_molecules.add(
                    self.medicine_molecule[:start]
                    + replacement
                    + self.medicine_molecule[end:]
                )

        return len(distinct_molecules)


class AdventOfCode2015Day19Part2(AdventOfCode2015Day19Part1):

    def get_answer(self):
        raise NotImplementedError()


if __name__ == "__main__":
    answer = AdventOfCode2015Day19Part2(DEFAULT_INPUT_FILE_PATH).get_answer()
    print(answer)
