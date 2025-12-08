import re
from dataclasses import dataclass
from pathlib import Path

from advent_of_code import AdventOfCode


DEFAULT_INPUT_FILE_PATH = Path(__file__).parent.joinpath("input.txt")


@dataclass
class Sue:
    number: int
    children: int | None = None
    cats: int | None = None
    samoyeds: int | None = None
    pomeranians: int | None = None
    akitas: int | None = None
    vizslas: int | None = None
    goldfish: int | None = None
    trees: int | None = None
    cars: int | None = None
    perfumes: int | None = None


class AdventOfCode2015Day16Part1(AdventOfCode):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.aunts: list[Sue] = []
        for number, things in re.findall(r"Sue (\d+): (.+)", self.input_data):

            aunt = Sue(number=int(number))
            for thing, count in re.findall(r"(\w+): (\d+)", things):
                setattr(aunt, thing, int(count))

            self.aunts.append(aunt)

        self.target_aunt = Sue(
            number=0,
            children=3,
            cats=7,
            samoyeds=2,
            pomeranians=3,
            akitas=0,
            vizslas=0,
            goldfish=5,
            trees=3,
            cars=2,
            perfumes=1,
        )

        self.things = (
            "children",
            "cats",
            "samoyeds",
            "pomeranians",
            "akitas",
            "vizslas",
            "goldfish",
            "trees",
            "cars",
            "perfumes",
        )

    def get_answer(self):
        for aunt in self.aunts:
            is_possible_aunt = True

            for thing in self.things:
                aunt_value = getattr(aunt, thing)
                target_aunt_value = getattr(self.target_aunt, thing)

                if aunt_value is None:
                    continue

                if aunt_value != target_aunt_value:
                    is_possible_aunt = False
                    break

            if is_possible_aunt:
                return aunt.number


class AdventOfCode2015Day16Part2(AdventOfCode2015Day16Part1):

    def get_answer(self):
        for aunt in self.aunts:
            is_possible_aunt = True

            for thing in self.things:
                aunt_value = getattr(aunt, thing)
                target_aunt_value = getattr(self.target_aunt, thing)

                if aunt_value is None:
                    continue

                if thing in ("cats", "trees"):
                    if aunt_value <= target_aunt_value:
                        is_possible_aunt = False
                        break

                elif thing in ("pomeranians", "goldfish"):
                    if aunt_value >= target_aunt_value:
                        is_possible_aunt = False
                        break

                elif aunt_value != target_aunt_value:
                    is_possible_aunt = False
                    break

            if is_possible_aunt:
                return aunt.number


if __name__ == "__main__":
    answer = AdventOfCode2015Day16Part2(DEFAULT_INPUT_FILE_PATH).get_answer()
    print(answer)
