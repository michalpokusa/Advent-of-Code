import re

from pathlib import Path

input_data = Path(__file__).parent.joinpath("input.txt").read_text()

start_wires_section, gates_section = input_data.split("\n\n")

values: dict[str, int] = dict()
for line in start_wires_section.split("\n"):
    wire, value = line.split(": ")
    values[wire] = int(value)


gates: dict[str, tuple[str, str, str]] = dict()
for line in gates_section.strip().split("\n"):
    _match = re.match(
        r"(?P<gate1>\w+) (?P<operation>AND|OR|XOR) (?P<gate2>\w+) -> (?P<output_gate>\w+)",
        line,
    )

    gate1, operation, gate2, output_gate = _match.groups()

    gates[output_gate] = (gate1, gate2, operation)

while gates:
    gates_to_remove = set()

    for output_gate, (input1, input2, operation) in gates.items():

        if not (input1 in values and input2 in values):
            continue

        match operation:
            case "AND":
                values[output_gate] = values[input1] & values[input2]
            case "OR":
                values[output_gate] = values[input1] | values[input2]
            case "XOR":
                values[output_gate] = values[input1] ^ values[input2]

        gates_to_remove.add(output_gate)

    for gate in gates_to_remove:
        gates.pop(gate)


z_values = sorted(
    [(key, value) for key, value in values.items() if key.startswith("z")]
)
bits = "".join(str(value) for _, value in z_values)[::-1]

print(int(bits, 2))
