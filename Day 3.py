import re


def read_data():
    with open("./data/day_3_input.txt", "r") as file:
        text = file.read()
    return text


def multiply_pattern(
    text="xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))",
):
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

    matches = re.findall(pattern, text)

    total_sum = 0
    for x, y in matches:
        total_sum += int(x) * int(y)

    return total_sum


def multiply_with_instructions(
    text="xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))",
):
    pattern = r"(do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\))"

    instructions = re.findall(pattern, text)

    enabled = True
    total_sum = 0

    for instruction in instructions:
        if instruction == "do()":
            enabled = True
        elif instruction == "don't()":
            enabled = False
        else:
            if enabled:
                match = re.match(r"mul\((\d{1,3}),(\d{1,3})\)", instruction)
                if match:
                    x, y = map(int, match.groups())
                    total_sum += x * y

    return total_sum


if __name__ == "__main__":
    print("NON-CORRUPTED OUTPUT : ", multiply_pattern(read_data()))
    print(
        "NON-CORRUPTED OUTPUT WITH INSTRUCTION: ",
        multiply_with_instructions(read_data()),
    )
