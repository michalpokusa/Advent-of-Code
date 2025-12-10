from dataclasses import dataclass
from itertools import combinations
from pathlib import Path
from advent_of_code import AdventOfCode


DEFAULT_EXAMPLE_INPUT_FILE_PATH = Path(__file__).parent.joinpath("example_input.txt")
DEFAULT_INPUT_FILE_PATH = Path(__file__).parent.joinpath("input.txt")


@dataclass
class Machine:
    goal_light_indicator_state: list[bool]
    goal_joltage_counter_state: list[int]
    buttons: list[tuple[int]]


class AdventOfCode2025Day10Part1(AdventOfCode):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.machines: list[Machine] = []

        manual = self.input_data.strip().splitlines()
        for line in manual:
            indicator_light_diagram, *button_wiring_schematics, joltage_requirements = (
                line.split(" ")
            )

            goal_light_indicator_state = [
                light == "#" for light in indicator_light_diagram.strip("[]")
            ]
            goal_joltage_counter_state = [
                int(joltage) for joltage in joltage_requirements.strip("{}").split(",")
            ]
            buttons = [
                tuple(int(idx) for idx in schematic.strip("()").split(","))
                for schematic in button_wiring_schematics
            ]
            self.machines.append(
                Machine(goal_light_indicator_state, goal_joltage_counter_state, buttons)
            )

    def fewest_button_presses(self, machine: Machine) -> int:
        for button_presses in range(1, len(machine.buttons) + 1):
            for button_combination in combinations(machine.buttons, button_presses):
                state = [False] * len(machine.goal_light_indicator_state)

                for button in button_combination:
                    for light_idx in button:
                        state[light_idx] = not state[light_idx]

                if state == machine.goal_light_indicator_state:
                    return button_presses

        raise ValueError("No combination of button presses can achieve the goal state.")

    def get_answer(self):
        return sum(self.fewest_button_presses(machine) for machine in self.machines)


class AdventOfCode2025Day10Part2(AdventOfCode2025Day10Part1):

    def fewest_button_presses(self, machine: Machine) -> int:
        raise NotImplementedError


if __name__ == "__main__":
    answer = AdventOfCode2025Day10Part2(DEFAULT_INPUT_FILE_PATH).get_answer()
    print(answer)
