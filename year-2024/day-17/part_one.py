class Computer:
    def __init__(
        self, register_A: int, register_B: int, register_C: int, program: list[int]
    ) -> None:
        self.register_A = register_A
        self.register_B = register_B
        self.register_C = register_C

        self.program = program
        self.instruction_pointer = 0

        self.output: list[int] = []

    def run_program(self) -> None:

        opcodes_to_instruction_map = {
            0: self.adv,
            1: self.bxl,
            2: self.bst,
            3: self.jnz,
            4: self.bxc,
            5: self.out,
            6: self.bdv,
            7: self.cdv,
        }

        while self.instruction_pointer < len(self.program):
            opcode = self.program[self.instruction_pointer]
            instruction = opcodes_to_instruction_map[opcode]
            operand = self.program[self.instruction_pointer + 1]

            instruction(operand)

            self.instruction_pointer += 2

    def _literal_operand(self, operand: int) -> int:
        return operand

    def _combo_operand(self, operand: int) -> int:
        match operand:
            case 0 | 1 | 2 | 3:
                return operand
            case 4:
                return self.register_A
            case 5:
                return self.register_B
            case 6:
                return self.register_C
            case 7:
                raise ValueError(f"Reserved combo operand: {operand}")
        raise ValueError(f"Invalid combo operand: {operand}")

    # The adv instruction (opcode 0) performs division. The numerator is the value in the A register.
    # The denominator is found by raising 2 to the power of the instruction's combo operand.
    # (So, an operand of 2 would divide A by 4 (2^2); an operand of 5 would divide A by 2^B.)
    # The result of the division operation is truncated to an integer and then written to the A register.
    def adv(self, operand: int) -> None:
        numerator = self.register_A
        combo_operand = self._combo_operand(operand)
        denominator = 2**combo_operand

        self.register_A = numerator // denominator

    # The bxl instruction (opcode 1) calculates the bitwise XOR of register B and the instruction's
    # literal operand, then stores the result in register B.
    def bxl(self, operand: int) -> None:
        bitewise_xor = self.register_B ^ self._literal_operand(operand)

        self.register_B = bitewise_xor

    # The bst instruction (opcode 2) calculates the value of its combo operand modulo 8
    # (thereby keeping only its lowest 3 bits), then writes that value to the B register.
    def bst(self, operand: int) -> None:
        combo_operand = self._combo_operand(operand)

        self.register_B = combo_operand % 8

    # The jnz instruction (opcode 3) does nothing if the A register is 0. However, if the A register
    # is not zero, it jumps by setting the instruction pointer to the value of its literal operand;
    # if this instruction jumps, the instruction pointer is not increased by 2 after this instruction.
    def jnz(self, operand: int) -> None:
        if self.register_A == 0:
            return

        self.instruction_pointer = self._literal_operand(operand) - 2

    # The bxc instruction (opcode 4) calculates the bitwise XOR of register B and register C, then
    # stores the result in register B. (For legacy reasons, this instruction reads an operand but ignores it.)
    def bxc(self, operand: int) -> None:
        bitewise_xor = self.register_B ^ self.register_C

        self.register_B = bitewise_xor

    # The out instruction (opcode 5) calculates the value of its combo operand modulo 8, then outputs
    # that value. (If a program outputs multiple values, they are separated by commas.)
    def out(self, operand: int) -> None:
        value = self._combo_operand(operand) % 8

        self.output.append(value)

    # The bdv instruction (opcode 6) works exactly like the adv instruction except that the result
    # is stored in the B register. (The numerator is still read from the A register.)
    def bdv(self, operand: int) -> None:
        numerator = self.register_A
        combo_operand = self._combo_operand(operand)
        denominator = 2**combo_operand

        self.register_B = numerator // denominator

    # The cdv instruction (opcode 7) works exactly like the adv instruction except that the result
    # is stored in the C register. (The numerator is still read from the A register.)
    def cdv(self, operand: int) -> None:
        numerator = self.register_A
        combo_operand = self._combo_operand(operand)
        denominator = 2**combo_operand

        self.register_C = numerator // denominator


computer = Computer(
    25986278,
    0,
    0,
    [2, 4, 1, 4, 7, 5, 4, 1, 1, 4, 5, 5, 0, 3, 3, 0],
)
computer.run_program()

print(",".join([str(value) for value in computer.output]))
