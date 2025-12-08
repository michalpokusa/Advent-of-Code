from itertools import combinations
from pathlib import Path
from advent_of_code import AdventOfCode


DEFAULT_EXAMPLE_INPUT_FILE_PATH = Path(__file__).parent.joinpath("example_input.txt")
DEFAULT_INPUT_FILE_PATH = Path(__file__).parent.joinpath("input.txt")


class AdventOfCode2025Day8Part1(AdventOfCode):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.junction_boxes_positions: list[tuple[int, int, int]] = [
            tuple(map(int, line.split(",")))
            for line in self.input_data.strip().splitlines()
        ]
        self.circuits: list[set[tuple[int, int, int]]] = [
            set([box]) for box in self.junction_boxes_positions
        ]
        self.distances: list[
            tuple[float, tuple[int, int, int], tuple[int, int, int]]
        ] = sorted(
            (self.euclidean_distance_between_boxes(box_a, box_b), box_a, box_b)
            for box_a, box_b in combinations(self.junction_boxes_positions, 2)
        )

    def euclidean_distance_between_boxes(
        self, coords1: tuple[int, int, int], coords2: tuple[int, int, int]
    ):
        x1, y1, z1 = coords1
        x2, y2, z2 = coords2
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2) ** 0.5

    def get_box_circuit(self, box: tuple[int, int, int]) -> int | None:
        for idx, circuit in enumerate(self.circuits):
            if box in circuit:
                return idx
        return None

    def connect_boxes(self, box_a: tuple[int, int, int], box_b: tuple[int, int, int]):
        box_a_circuit_idx = self.get_box_circuit(box_a)
        box_b_circuit_idx = self.get_box_circuit(box_b)

        # Because these two junction boxes were already in the same circuit, nothing happens!
        if box_a_circuit_idx is not None and box_a_circuit_idx == box_b_circuit_idx:
            return

        # If both boxes are in different circuits, merge the circuits
        if box_a_circuit_idx is not None and box_b_circuit_idx is not None:
            circuit_a = self.circuits[box_a_circuit_idx]
            circuit_b = self.circuits[box_b_circuit_idx]

            self.circuits[box_a_circuit_idx] = circuit_a.union(circuit_b)
            del self.circuits[box_b_circuit_idx]
            return

        # If one box is in a circuit, add the other box to that circuit
        if box_a_circuit_idx is not None or box_b_circuit_idx is not None:
            if box_a_circuit_idx is not None:
                self.circuits[box_a_circuit_idx].add(box_b)
            elif box_b_circuit_idx is not None:
                self.circuits[box_b_circuit_idx].add(box_a)
            return

        raise RuntimeError("Unreachable code reached!")

    def get_answer(self):

        for distance, box_a, box_b in self.distances[:1000]:
            self.connect_boxes(box_a, box_b)

        three_largest_circuits = sorted(self.circuits, key=len, reverse=True)[:3]
        answer = 1
        for circuit in three_largest_circuits:
            answer *= len(circuit)

        return answer


class AdventOfCode2025Day8Part2(AdventOfCode2025Day8Part1):

    def get_answer(self):

        for distance, box_a, box_b in self.distances:
            self.connect_boxes(box_a, box_b)

            if len(self.circuits) == 1:
                break

        x_a, _, _ = box_a
        x_b, _, _ = box_b
        return x_a * x_b


if __name__ == "__main__":
    answer = AdventOfCode2025Day8Part2(DEFAULT_INPUT_FILE_PATH).get_answer()
    print(answer)
