import re
from pathlib import Path

from advent_of_code import AdventOfCode


DEFAULT_EXAMPLE_INPUT_FILE_PATH = Path(__file__).parent.joinpath("example_input.txt")
DEFAULT_INPUT_FILE_PATH = Path(__file__).parent.joinpath("input.txt")


class AdventOfCode2015Day7Part1(AdventOfCode):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        wires = set(re.findall(r"\-> (\w+)", self.input_data))
        self.signals = {wire: None for wire in wires}
        self.instructions = re.findall(
            r"(?:(?:(\w+) )?(AND|OR|LSHIFT|RSHIFT|NOT) )?(\w+) -> (\w+)",
            self.input_data,
        )

    def is_wire(self, value: str):
        return value in self.signals

    def get_answer(self):
        while self.instructions:
            for left_value, operation, right_value, target in self.instructions:

                if self.signals[target] is not None:
                    continue

                required_signals = []
                if operation in ("LSHIFT", "RSHIFT", "AND", "OR"):
                    if self.is_wire(left_value):
                        required_signals.append(left_value)
                if operation in ("NOT", "AND", "OR", ""):
                    if self.is_wire(right_value):
                        required_signals.append(right_value)

                if not all(
                    self.signals[signal] is not None for signal in required_signals
                ):
                    continue

                if operation == "":
                    self.signals[target] = (
                        self.signals[right_value]
                        if self.is_wire(right_value)
                        else int(right_value)
                    )
                if operation == "AND":
                    self.signals[target] = (
                        self.signals[left_value]
                        if self.is_wire(left_value)
                        else int(left_value)
                    ) & (
                        self.signals[right_value]
                        if self.is_wire(right_value)
                        else int(right_value)
                    )
                elif operation == "OR":
                    self.signals[target] = (
                        self.signals[left_value]
                        if self.is_wire(left_value)
                        else int(left_value)
                    ) | (
                        self.signals[right_value]
                        if self.is_wire(right_value)
                        else int(right_value)
                    )
                elif operation == "LSHIFT":
                    self.signals[target] = self.signals[left_value] << int(right_value)
                elif operation == "RSHIFT":
                    self.signals[target] = self.signals[left_value] >> int(right_value)
                elif operation == "NOT":
                    self.signals[target] = ~self.signals[right_value] & 65535

            self.instructions = [
                instruction
                for instruction in self.instructions
                if self.signals[instruction[3]] is None
            ]

        return self.signals["a"]


class AdventOfCode2015Day7Part2(AdventOfCode2015Day7Part1):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.signals["b"] = 956


if __name__ == "__main__":
    answer = AdventOfCode2015Day7Part2(DEFAULT_INPUT_FILE_PATH).get_answer()
    print(answer)
