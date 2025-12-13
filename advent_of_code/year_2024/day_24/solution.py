import re
from collections import defaultdict
from dataclasses import dataclass
from copy import copy
from pathlib import Path

from advent_of_code import AdventOfCode


DEFAULT_PART1_EXAMPLE_INPUT_FILE_PATH = Path(__file__).parent.joinpath(
    "part1_example_input.txt"
)
DEFAULT_PART2_EXAMPLE_INPUT_FILE_PATH = Path(__file__).parent.joinpath(
    "part2_example_input.txt"
)
DEFAULT_INPUT_FILE_PATH = Path(__file__).parent.joinpath("input.txt")


@dataclass
class Gate:
    input1: str
    input2: str
    operation: str
    output: str


class AdventOfCode2024Day24Part1(AdventOfCode):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        start_wires_section, gates_section = self.input_data.split("\n\n")

        self.values: dict[str, int | None] = defaultdict(int)

        self.gates: list[Gate] = []
        for line in gates_section.strip().split("\n"):
            match_ = re.match(
                r"(?P<gate1>\w+) (?P<operation>AND|OR|XOR) (?P<gate2>\w+) -> (?P<output_gate>\w+)",
                line,
            )
            gate1, operation, gate2, output_gate = match_.groups()

            self.gates.append(Gate(gate1, gate2, operation, output_gate))

            self.values.setdefault(gate1, None)
            self.values.setdefault(gate2, None)
            self.values.setdefault(output_gate, None)

        for line in start_wires_section.split("\n"):
            wire, value = line.split(": ")
            self.values[wire] = int(value)

    def get_number_from_wires(
        self, values: dict[str, int | None], wire_prefix: str
    ) -> int:
        bit_values = sorted(
            [
                (key, value)
                for key, value in values.items()
                if key.startswith(wire_prefix)
            ]
        )
        bits = "".join(str(value) for _, value in bit_values)[::-1]
        return int(bits, 2)

    def simulate_gates(
        self, values: dict[str, int | None], gates: list[Gate]
    ) -> dict[str, int | None]:
        values_copy = copy(values)

        while any(value is None for value in values_copy.values()):
            for gate in gates:

                if values_copy[gate.input1] is None or values_copy[gate.input2] is None:
                    continue

                match gate.operation:
                    case "AND":
                        values_copy[gate.output] = (
                            values_copy[gate.input1] & values_copy[gate.input2]
                        )
                    case "OR":
                        values_copy[gate.output] = (
                            values_copy[gate.input1] | values_copy[gate.input2]
                        )
                    case "XOR":
                        values_copy[gate.output] = (
                            values_copy[gate.input1] ^ values_copy[gate.input2]
                        )

        return values_copy

    def get_answer(self):
        values = self.simulate_gates(self.values, self.gates)

        return self.get_number_from_wires(values, "z")


class AdventOfCode2024Day24Part2(AdventOfCode2024Day24Part1):

    def get_answer(self):
        raise NotImplementedError


if __name__ == "__main__":
    answer = AdventOfCode2024Day24Part2(DEFAULT_INPUT_FILE_PATH).get_answer()
    print(answer)
