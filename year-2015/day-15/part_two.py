import re

from dataclasses import dataclass
from itertools import product
from pathlib import Path

input_data = Path(__file__).parent.joinpath("input.txt").read_text().strip()


LINE_PATTERN = re.compile(
    r"(?P<ingredient>\w+): capacity (?P<capacity>-?\d+), durability (?P<durability>-?\d+), flavor (?P<flavor>-?\d+), texture (?P<texture>-?\d+), calories (?P<calories>-?\d+)"
)


@dataclass
class Ingredient:
    name: str
    capacity: int
    durability: int
    flavor: int
    texture: int
    calories: int


ingredients: list[Ingredient] = []

for line in input_data.split("\n"):
    _match = re.match(LINE_PATTERN, line)

    ingredient, capacity, durability, flavor, texture, calories = _match.groups()

    ingredients.append(
        Ingredient(
            ingredient,
            int(capacity),
            int(durability),
            int(flavor),
            int(texture),
            int(calories),
        )
    )

different_ingredients = len(ingredients)


def get_cookie_calories(proportions: list[int]) -> int:
    total_calories = 0

    for ingredient_idx, proportion in enumerate(proportions):
        ingredient = ingredients[ingredient_idx]

        total_calories += ingredient.calories * proportion

    return total_calories


def get_cookie_score(proportions: list[int]) -> int:
    total_capacity = 0
    total_durability = 0
    total_flavor = 0
    total_texture = 0

    for ingredient_idx, proportion in enumerate(proportions):
        ingredient = ingredients[ingredient_idx]

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


total_cookie_ingredients = 100

max_cookie_score = 0

for combination in product(range(101), repeat=different_ingredients):
    if sum(combination) != total_cookie_ingredients:
        continue

    cookie_calories = get_cookie_calories(combination)

    if cookie_calories != 500:
        continue

    cookie_score = get_cookie_score(combination)

    if max_cookie_score < cookie_score:
        max_cookie_score = cookie_score


print(max_cookie_score)
