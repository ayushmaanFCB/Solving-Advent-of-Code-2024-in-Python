def read_data():
    registers = []
    program = None
    with open("data/day_17_input.txt", "r") as file:
        data = file.readlines()
        for line in data:
            line = line.strip("\n")
            if line.startswith("Register"):
                registers.append(int(line.split(": ")[1]))
            if line.startswith("Program"):
                program = list(map(int, line.split(": ")[1].split(",")))
    return registers, program


# PART 1
def simulate_program(registers=[729, 0, 0], program=[0, 1, 5, 4, 3, 0]):
    A, B, C = registers
    ip = 0
    output = []

    def get_combo_value(op):
        if op <= 3:
            return op
        if op == 4:
            return A
        if op == 5:
            return B
        if op == 6:
            return C
        raise ValueError("Invalid combo operand")

    while ip < len(program):
        opcode = program[ip]
        operand = program[ip + 1] if ip + 1 < len(program) else 0

        if opcode == 0:
            A //= 2 ** get_combo_value(operand)
        elif opcode == 1:
            B ^= operand
        elif opcode == 2:
            B = get_combo_value(operand) % 8
        elif opcode == 3:
            if A != 0:
                ip = operand
                continue
        elif opcode == 4:
            B ^= C
        elif opcode == 5:
            output.append(get_combo_value(operand) % 8)
        elif opcode == 6:
            B = A // (2 ** get_combo_value(operand))
        elif opcode == 7:
            C = A // (2 ** get_combo_value(operand))
        else:
            raise ValueError(f"Unknown opcode: {opcode}")

        ip += 2

    return ",".join(map(str, output))


if __name__ == "__main__":
    registers, program = read_data()
    output = simulate_program(registers=registers, program=program)
    print(output)
