import json

from pathlib import Path

input_data = Path(__file__).parent.joinpath("input.txt").read_text()

json_document = json.loads(input_data)

sum_of_all_numbers = 0


def process_json_data(element: int | str | list | dict) -> None:
    global sum_of_all_numbers

    if isinstance(element, int):
        sum_of_all_numbers += element

    elif isinstance(element, str):
        pass

    elif isinstance(element, list):
        for item in element:
            process_json_data(item)

    elif isinstance(element, dict):
        if "red" in element.values():
            return

        for item in element.values():
            process_json_data(item)


process_json_data(json_document)

print(sum_of_all_numbers)
