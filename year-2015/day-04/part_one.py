from hashlib import md5

input_data = "ckczppom"


number = 1

while True:
    data = f"{input_data}{number}"
    hash = md5(data.encode()).hexdigest()

    if hash.startswith("00000"):
        break

    number += 1

print(number)
