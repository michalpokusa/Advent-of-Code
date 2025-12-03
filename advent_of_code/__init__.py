from pathlib import Path


class AdventOfCode:

    def __init__(self, input_file_path: Path) -> None:
        self.input_file_path = input_file_path
        self.input_data = self.input_file_path.read_text()

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.input_file_path}')"
