import re
from dataclasses import dataclass
from itertools import product
from pathlib import Path

from advent_of_code import AdventOfCode


DEFAULT_EXAMPLE_INPUT_FILE_PATH = Path(__file__).parent.joinpath("example_input.txt")
DEFAULT_INPUT_FILE_PATH = Path(__file__).parent.joinpath("input.txt")


@dataclass
class Ingredient:
    name: str
    capacity: int
    durability: int
    flavor: int
    texture: int
    calories: int


class AdventOfCode2015Day15Part1(AdventOfCode):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        lines = self.input_data.strip().splitlines()
        self.ingredients: list[Ingredient] = []
        pattern = re.compile(
            r"(?P<name>\w+): capacity (?P<capacity>-?\d+), durability (?P<durability>-?\d+), flavor (?P<flavor>-?\d+), texture (?P<texture>-?\d+), calories (?P<calories>-?\d+)"
        )
        for line in lines:
            match = re.match(pattern, line)
            name, capacity, durability, flavor, texture, calories = match.groups()

            self.ingredients.append(
                Ingredient(
                    name,
                    int(capacity),
                    int(durability),
                    int(flavor),
                    int(texture),
                    int(calories),
                )
            )

    def get_cookie_score(self, proportions: list[int]) -> int:
        total_capacity = 0
        total_durability = 0
        total_flavor = 0
        total_texture = 0

        for ingredient_idx, proportion in enumerate(proportions):
            ingredient = self.ingredients[ingredient_idx]

            total_capacity += ingredient.capacity * proportion
            total_durability += ingredient.durability * proportion
            total_flavor += ingredient.flavor * proportion
            total_texture += ingredient.texture * proportion

        return (
            max(0, total_capacity)
            * max(0, total_durability)
            * max(0, total_flavor)
            * max(0, total_texture)
        )

    def get_answer(self):
        total_cookie_ingredients = 100
        max_cookie_score = 0

        for combination in product(range(101), repeat=len(self.ingredients)):
            if sum(combination) != total_cookie_ingredients:
                continue

            cookie_score = self.get_cookie_score(combination)

            if max_cookie_score < cookie_score:
                max_cookie_score = cookie_score

        return max_cookie_score


class AdventOfCode2015Day15Part2(AdventOfCode2015Day15Part1):

    def get_cookie_calories(self, proportions: list[int]) -> int:
        total_calories = 0

        for ingredient_idx, proportion in enumerate(proportions):
            ingredient = self.ingredients[ingredient_idx]
            total_calories += ingredient.calories * proportion

        return total_calories

    def get_answer(self):
        total_cookie_ingredients = 100
        max_cookie_score = 0

        for combination in product(range(101), repeat=len(self.ingredients)):
            if sum(combination) != total_cookie_ingredients:
                continue

            if self.get_cookie_calories(combination) != 500:
                continue

            cookie_score = self.get_cookie_score(combination)

            if max_cookie_score < cookie_score:
                max_cookie_score = cookie_score

        return max_cookie_score


if __name__ == "__main__":
    answer = AdventOfCode2015Day15Part2(DEFAULT_INPUT_FILE_PATH).get_answer()
    print(answer)
