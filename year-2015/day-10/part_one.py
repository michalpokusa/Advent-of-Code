import re

input_data = "1113222113"


def look_and_say(_input: str) -> str:
    result = ""
    for match in re.finditer(r"(1+|2+|3+|4+|5+|6+|7+|8+|9+|0+)", _input):
        result += str(len(match.group(0))) + match.group(0)[0]

    return result


for _ in range(40):
    input_data = look_and_say(input_data)

print(len(input_data))
