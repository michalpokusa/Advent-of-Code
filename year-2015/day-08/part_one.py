from pathlib import Path


input_data = Path(__file__).parent.joinpath("input.txt").read_text()

lines = [line for line in input_data.split("\n") if line]

total_in_memory_characters = 0

for line in lines:

    code_characters = len(line)
    memory_characters = len(eval(line))

    total_in_memory_characters += code_characters - memory_characters

print(total_in_memory_characters)
