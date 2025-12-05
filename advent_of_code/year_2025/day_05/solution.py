from itertools import pairwise

from pathlib import Path
from advent_of_code import AdventOfCode


DEFAULT_EXAMPLE_INPUT_FILE_PATH = Path(__file__).parent.joinpath("example_input.txt")
DEFAULT_INPUT_FILE_PATH = Path(__file__).parent.joinpath("input.txt")


class AdventOfCode2025Day5Part1(AdventOfCode):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        input_data_part1, input_data_part2 = self.input_data.strip().split("\n\n")

        self.fresh_ingredient_id_ranges = [
            tuple(map(int, line.strip().split("-")))
            for line in input_data_part1.strip().split("\n")
        ]
        self.available_ingredient_ids = list(
            map(int, input_data_part2.strip().split("\n"))
        )

    def is_ingredient_fresh(self, ingredient_id: int) -> bool:
        for range_start, range_end in self.fresh_ingredient_id_ranges:
            if range_start <= ingredient_id <= range_end:
                return True
        return False

    def get_answer(self) -> int:
        fresh_ingredients = 0

        for ingredient_id in self.available_ingredient_ids:
            if self.is_ingredient_fresh(ingredient_id):
                fresh_ingredients += 1

        return fresh_ingredients


class AdventOfCode2025Day5Part2(AdventOfCode2025Day5Part1):

    def get_answer(self) -> int:
        ingredient_ids_considered_fresh = 0

        ranges_edge_points = sorted(
            set(
                point
                for id_range in self.fresh_ingredient_id_ranges
                for point in id_range
            )
        )

        # id_ranges_from_edge_points = (
        #     (ranges_edge_points[i], ranges_edge_points[i + 1])
        #     for i in range(len(ranges_edge_points) - 1)
        # )
        id_ranges_from_edge_points = pairwise(ranges_edge_points)

        for range_start, range_end in id_ranges_from_edge_points:
            number_inside_range = range_start + (range_end - range_start) // 2

            if self.is_ingredient_fresh(number_inside_range):
                ingredient_ids_considered_fresh += max(range_end - range_start - 1, 0)

        ingredient_ids_considered_fresh += len(ranges_edge_points)

        return ingredient_ids_considered_fresh


if __name__ == "__main__":
    answer = AdventOfCode2025Day5Part2(DEFAULT_INPUT_FILE_PATH).get_answer()
    print(answer)
