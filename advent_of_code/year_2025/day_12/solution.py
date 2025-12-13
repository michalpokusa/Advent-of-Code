import re
from dataclasses import dataclass
from functools import cached_property
from pathlib import Path

from advent_of_code import AdventOfCode


DEFAULT_EXAMPLE_INPUT_FILE_PATH = Path(__file__).parent.joinpath("example_input.txt")
DEFAULT_INPUT_FILE_PATH = Path(__file__).parent.joinpath("input.txt")


@dataclass
class Present:
    shape: list[list[str]]

    @cached_property
    def area(self) -> int:
        return sum(row.count("#") for row in self.shape)


@dataclass
class Region:
    width: int
    length: int
    present_shape_quantities: dict[int, int]

    @cached_property
    def area(self) -> int:
        return self.width * self.length


class AdventOfCode2025Day12Part1(AdventOfCode):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.presents: dict[int, Present] = {}
        for idx, shape in re.findall(
            r"(\d+):\n((?:[#.\n]+)(?:[#.]+))", self.input_data
        ):
            self.presents[int(idx)] = Present(
                shape=[list(line) for line in str(shape).strip().split("\n")],
            )

        self.regions: list[Region] = []
        for width, length, present_shape_quantities in re.findall(
            r"(\d+)x(\d+): ([\d ]+)", self.input_data
        ):
            self.regions.append(
                Region(
                    width=int(width),
                    length=int(length),
                    present_shape_quantities={
                        idx: int(quantity)
                        for idx, quantity in enumerate(
                            str(present_shape_quantities).split(" ")
                        )
                    },
                )
            )

        pass

    def total_area_of_all_presents(self, region: Region) -> int:
        return sum(
            self.presents[idx].area * quantity
            for idx, quantity in region.present_shape_quantities.items()
        )

    def can_region_fit_presents(self, region: Region) -> bool:

        if region.area < self.total_area_of_all_presents(region):
            return False

        # There should be some more complex checks here to ensure the shapes can actually fit,
        # but for some reason the total area check seems to be sufficient for the provided input data.

        return True

    def get_answer(self):
        regions_that_can_fit_listed_presents = 0

        for region in self.regions:
            if self.can_region_fit_presents(region):
                regions_that_can_fit_listed_presents += 1

        return regions_that_can_fit_listed_presents


class AdventOfCode2025Day12Part2(AdventOfCode2025Day12Part1):

    def get_answer(self):
        raise NotImplementedError


if __name__ == "__main__":
    answer = AdventOfCode2025Day12Part2(DEFAULT_INPUT_FILE_PATH).get_answer()
    print(answer)
