def run_intcode(program):
    index = 0
    while True:
        opcode = program[index]
        if opcode == 1:
            # Addition
            operand1 = program[program[index + 1]]
            operand2 = program[program[index + 2]]
            result_index = program[index + 3]
            program[result_index] = operand1 + operand2
            index += 4
        elif opcode == 2:
            # Multiplication
            operand1 = program[program[index + 1]]
            operand2 = program[program[index + 2]]
            result_index = program[index + 3]
            program[result_index] = operand1 * operand2
            index += 4
        elif opcode == 99:
            # Halt
            break
        else:
            # Unknown opcode
            break
    
    return program[0]

# Input program
program = [
    1, 12, 2, 3,
    1, 1, 2, 3,
    1, 3, 4, 3,
    1, 1, 5, 0,
    99,
    30, 40, 50
]

# Make a copy of the original program to avoid modifying it directly
program_copy = program[:]
result = run_intcode(program_copy)
print("Value left at position 0 after halting:", result)