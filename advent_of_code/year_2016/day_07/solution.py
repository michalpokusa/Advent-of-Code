import re
from pathlib import Path

from advent_of_code import AdventOfCode


DEFAULT_EXAMPLE_INPUT_FILE_PATH = Path(__file__).parent.joinpath("example_input.txt")
DEFAULT_INPUT_FILE_PATH = Path(__file__).parent.joinpath("input.txt")


class AdventOfCode2016Day7Part1(AdventOfCode):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.ipv7_addresses = self.input_data.strip().splitlines()

    def has_abba(self, segment: str) -> bool:
        return bool(re.search(r"(.)(?!\1)(.)\2\1", segment))

    def supports_tls(self, address: str) -> bool:
        supernet_sequences = re.split(r"\[.*?\]", address)
        hypernet_sequences = re.findall(r"\[(.*?)\]", address)

        return any(self.has_abba(part) for part in supernet_sequences) and not any(
            self.has_abba(part) for part in hypernet_sequences
        )

    def get_answer(self):
        return len(list(filter(self.supports_tls, self.ipv7_addresses)))


class AdventOfCode2016Day7Part2(AdventOfCode2016Day7Part1):

    def get_all_aba(self, sequences: list[str]) -> set[tuple[str, str]]:
        aba_patterns = set()
        for sequence in sequences:
            for i in range(len(sequence) - 2):
                a, b, c = sequence[i : i + 3]
                if a == c and a != b:
                    aba_patterns.add(f"{a}{b}{a}")
        return aba_patterns

    def get_all_bab(self, sequences: list[str]) -> set[str]:
        return self.get_all_aba(sequences)

    def get_bab_for_aba(self, aba: str) -> set[str]:
        a, b, _ = aba
        return f"{b}{a}{b}"

    def supports_ssl(self, address: str) -> bool:
        supernet_sequences = re.split(r"\[.*?\]", address)
        hypernet_sequences = re.findall(r"\[(.*?)\]", address)

        aba_patterns = self.get_all_aba(supernet_sequences)
        corresponding_bab_patterns = set(
            self.get_bab_for_aba(aba) for aba in aba_patterns
        )
        bab_patterns = self.get_all_bab(hypernet_sequences)

        return bab_patterns.intersection(corresponding_bab_patterns) != set()

    def get_answer(self):
        return len(list(filter(self.supports_ssl, self.ipv7_addresses)))


if __name__ == "__main__":
    answer = AdventOfCode2016Day7Part2(DEFAULT_INPUT_FILE_PATH).get_answer()
    print(answer)
