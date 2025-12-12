from pathlib import Path

from advent_of_code import AdventOfCode


DEFAULT_EXAMPLE_INPUT_FILE_PATH = Path(__file__).parent.joinpath("example_input.txt")
DEFAULT_INPUT_FILE_PATH = Path(__file__).parent.joinpath("input.txt")


class AdventOfCode2024Day12Part1(AdventOfCode):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.farm_map = [
            list(row.strip()) for row in self.input_data.split("\n") if row.strip()
        ]

    def is_inside_map(self, map: list[list[str]], y: int, x: int) -> bool:
        return 0 <= y < len(map) and 0 <= x < len(map[0])

    def get_region_plots(
        self, map: list[list[str]], y: int, x: int
    ) -> set[tuple[int, int]]:
        plant_type = map[y][x]
        plots = {(y, x)}
        visited_plots = {(y, x)}

        def area_expands_here(y: int, x: int):
            return (
                self.is_inside_map(map, y, x)
                and map[y][x] == plant_type
                and (y, x) not in visited_plots
            )

        while plots:
            y, x = plots.pop()

            # Up
            if area_expands_here(y - 1, x):
                plots.add((y - 1, x))
                visited_plots.add((y - 1, x))

            # Right
            if area_expands_here(y, x + 1):
                plots.add((y, x + 1))
                visited_plots.add((y, x + 1))

            # Down
            if area_expands_here(y + 1, x):
                plots.add((y + 1, x))
                visited_plots.add((y + 1, x))

            # Left
            if area_expands_here(y, x - 1):
                plots.add((y, x - 1))
                visited_plots.add((y, x - 1))

        return visited_plots

    def get_region_area(self, map: list[list[str]], y: int, x: int) -> int:
        return len(self.get_region_plots(map, y, x))

    def get_region_perimeter(self, map: list[list[str]], y: int, x: int) -> int:
        plant_type = map[y][x]
        plots = {(y, x)}
        visited_plots = {(y, x)}

        def area_expands_here(y: int, x: int):
            return (
                self.is_inside_map(map, y, x)
                and map[y][x] == plant_type
                and (y, x) not in visited_plots
            )

        fences = 0

        while plots:
            y, x = plots.pop()

            # Up
            if area_expands_here(y - 1, x):
                plots.add((y - 1, x))
                visited_plots.add((y - 1, x))
            else:
                if (y - 1, x) not in visited_plots:
                    fences += 1

            # Right
            if area_expands_here(y, x + 1):
                plots.add((y, x + 1))
                visited_plots.add((y, x + 1))
            else:
                if (y, x + 1) not in visited_plots:
                    fences += 1

            # Down
            if area_expands_here(y + 1, x):
                plots.add((y + 1, x))
                visited_plots.add((y + 1, x))
            else:
                if (y + 1, x) not in visited_plots:
                    fences += 1

            # Left
            if area_expands_here(y, x - 1):
                plots.add((y, x - 1))
                visited_plots.add((y, x - 1))
            else:
                if (y, x - 1) not in visited_plots:
                    fences += 1

        return fences

    def mark_region_as_fenced(self, map: list[list[str]], y: int, x: int) -> None:
        plant_type = map[y][x]
        plots = {(y, x)}

        while plots:
            y, x = plots.pop()

            # Mark as fenced
            map[y][x] = "."

            # Up
            if self.is_inside_map(map, y - 1, x) and map[y - 1][x] == plant_type:
                plots.add((y - 1, x))

            #  Right
            if self.is_inside_map(map, y, x + 1) and map[y][x + 1] == plant_type:
                plots.add((y, x + 1))

            # Down
            if self.is_inside_map(map, y + 1, x) and map[y + 1][x] == plant_type:
                plots.add((y + 1, x))

            # Left
            if self.is_inside_map(map, y, x - 1) and map[y][x - 1] == plant_type:
                plots.add((y, x - 1))

    def get_answer(self):
        farm_map = [row.copy() for row in self.farm_map]

        total_fencing_price = 0

        for y in range(len(farm_map)):
            for x in range(len(farm_map[y])):
                if farm_map[y][x] == ".":
                    continue

                area = self.get_region_area(farm_map, y, x)
                perimeter = self.get_region_perimeter(farm_map, y, x)

                fencing_price = area * perimeter

                total_fencing_price += fencing_price

                self.mark_region_as_fenced(farm_map, y, x)

        return total_fencing_price


class AdventOfCode2024Day12Part2(AdventOfCode2024Day12Part1):

    def get_region_number_of_sides(
        self, map: list[list[str]], plot_y: int, plot_x: int
    ) -> int:
        region_plots = self.get_region_plots(map, plot_y, plot_x)
        region_fences = set()

        for plot_y, plot_x in region_plots:
            # Up
            if (plot_y - 1, plot_x) not in region_plots:
                region_fences.add((plot_y, plot_x, "up"))

            # Right
            if (plot_y, plot_x + 1) not in region_plots:
                region_fences.add((plot_y, plot_x, "right"))

            # Down
            if (plot_y + 1, plot_x) not in region_plots:
                region_fences.add((plot_y, plot_x, "down"))

            # Left
            if (plot_y, plot_x - 1) not in region_plots:
                region_fences.add((plot_y, plot_x, "left"))

        sides = 0

        def remove_connected_fences(
            y: int, x: int, dy: int, dx: int, direction: str
        ) -> None:
            connected_fence = (y + dy, x + dx, direction)
            while connected_fence in region_fences:
                region_fences.remove(connected_fence)
                _y, _x, _direction = connected_fence
                connected_fence = (_y + dy, _x + dx, _direction)

        while region_fences:
            sides += 1

            plot_y, plot_x, direction = region_fences.pop()

            # Up connected fences
            remove_connected_fences(plot_y, plot_x, -1, 0, direction)

            # Right connected fences
            remove_connected_fences(plot_y, plot_x, 0, 1, direction)

            # Down connected fences
            remove_connected_fences(plot_y, plot_x, 1, 0, direction)

            # Left connected fences
            remove_connected_fences(plot_y, plot_x, 0, -1, direction)

        return sides

    def mark_region_as_fenced(self, map: list[list[str]], y: int, x: int) -> None:
        plant_type = map[y][x]
        plots = {(y, x)}

        while plots:
            y, x = plots.pop()

            # Mark as fenced
            map[y][x] = "."

            # Up
            if self.is_inside_map(map, y - 1, x) and map[y - 1][x] == plant_type:
                plots.add((y - 1, x))

            #  Right
            if self.is_inside_map(map, y, x - 1) and map[y][x - 1] == plant_type:
                plots.add((y, x - 1))

            # Down
            if self.is_inside_map(map, y + 1, x) and map[y + 1][x] == plant_type:
                plots.add((y + 1, x))

            # Left
            if self.is_inside_map(map, y, x + 1) and map[y][x + 1] == plant_type:
                plots.add((y, x + 1))

    def get_answer(self):
        farm_map = [row.copy() for row in self.farm_map]
        total_fencing_price = 0

        for y in range(len(farm_map)):
            for x in range(len(farm_map[y])):

                if farm_map[y][x] == ".":
                    continue

                area = self.get_region_area(farm_map, y, x)
                number_of_sides = self.get_region_number_of_sides(farm_map, y, x)

                fencing_price = area * number_of_sides

                total_fencing_price += fencing_price

                self.mark_region_as_fenced(farm_map, y, x)

        return total_fencing_price


if __name__ == "__main__":
    answer = AdventOfCode2024Day12Part2(DEFAULT_INPUT_FILE_PATH).get_answer()
    print(answer)
