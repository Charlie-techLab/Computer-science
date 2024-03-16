'''
Title: CPU Simulator Documentation

Description:
The provided code simulates the functionality of a Central Processing Unit
(CPU). It defines a CPU class with various methods to execute instructions
such as arithmetic operations, memory management, and control flow operations.
The CPU operates on a program provided as a list of instructions.

Class:
CPU

Methods:
1. run(program)
   - Description: Executes the provided program by interpreting each
     instruction.
   - Parameters:
     - program: A list of instructions to be executed by the CPU.
   - Behavior:
     - Iterates over each instruction in the program.
     - Executes the corresponding operation based on the instruction name.
     - Continues execution until encountering a HALT instruction.

2. ADD(arg1, arg2, result)
   - Description: Performs addition operation and stores the result in the
     specified register.
   - Parameters:
     - arg1: Name of the first operand register.
     - arg2: Name of the second operand register.
     - result: Name of the register to store the result.

3. SUB(arg1, arg2, result)
   - Description: Performs subtraction operation and stores the result in the
     specified register.
   - Parameters:
     - arg1: Name of the first operand register.
     - arg2: Name of the second operand register.
     - result: Name of the register to store the result.

4. MUL(arg1, arg2, result)
   - Description: Performs multiplication operation and stores the result in
     the specified register.
   - Parameters:
     - arg1: Name of the first operand register.
     - arg2: Name of the second operand register.
     - result: Name of the register to store the result.

5. DIV(arg1, arg2, result)
   - Description: Performs division operation and stores the result in the
     specified register.
   - Parameters:
     - arg1: Name of the first operand register.
     - arg2: Name of the second operand register.
     - result: Name of the register to store the result.

6. INC(arg1)
   - Description: Increments the value in the specified register by 1.
   - Parameters:
     - arg1: Name of the register to be incremented.

7. DEC(arg1)
   - Description: Decrements the value in the specified register by 1.
   - Parameters:
     - arg1: Name of the register to be decremented.

8. CMP(op, arg1, arg2, result)
   - Description: Compares the values in two registers and stores the result in
     the specified register based on the comparison operator.
   - Parameters:
     - op: Comparison operator (<, >, <=, >=, ==, !=).
     - arg1: Name of the first operand register.
     - arg2: Name of the second operand register.
     - result: Name of the register to store the result.

9. CONST(value, arg1)
   - Description: Stores a constant value in the specified register.
   - Parameters:
     - value: Constant value to be stored.
     - arg1: Name of the register to store the value.

10. LOAD(rs, rd, offset)
   - Description: Loads a value from memory into the specified register.
   - Parameters:
     - rs: Name of the source register containing the memory address.
     - rd: Name of the destination register to store the loaded value.
     - offset: Offset value to access memory.

11. STORE(rs, rd, offset)
   - Description: Stores the value from the specified register into memory.
   - Parameters:
     - rs: Name of the source register containing the value to be stored.
     - rd: Name of the register containing the memory address.
     - offset: Offset value to access memory.

12. JMP(arg1, offset)
   - Description: Jumps to the specified memory address.
   - Parameters:
     - arg1: Name of the register containing the memory address.
     - offset: Offset value to adjust the memory address.

13. JZ(arg1, arg2)
   - Description: Jumps to the specified memory address if the value in the
     second register is zero.
   - Parameters:
     - arg1: Name of the register containing the memory address.
     - arg2: Name of the register to check for zero value.

14. HALT()
   - Description: Halts the execution of the program.

Usage:
- Create an instance of the CPU class.
- Define a program as a list of instructions.
- Call the run method of the CPU instance with the program as an argument to
  execute the program.
- View the console output to observe the execution flow and results of each
  instruction.

Example:
machine = CPU()
code = [
    ('CONST', 10, 'Ra'),
    ('CONST', 20, 'Rb'),
    ('ADD', 'Ra', 'Rb', 'Rc'),
    ('HALT',)
]
machine.run(code)

'''

class CPU:
    def run(self, program):
        self.registers = {
            "Ra": 0,
            "Rb": 0,
            "Rc": 0,
            "Rd": 0,
            "Re": 0,
            "Rf": 0,
            "Rg": 0,
            "Rh": 0,
            "IP": 0,  # Instruction Pointer
            "SP": 0   # Stack Pointer
        }

        self.memory = [0] * 1024  # 1024 bytes

        while True:
            instruction = program[self.registers["IP"]]
            print("Executing:", instruction)

            self.registers["IP"] += 1

            name = instruction[0]

            if name == "ADD":
                self.ADD(instruction[1], instruction[2], instruction[3])
            elif name == "SUBSTRACT":
                self.SUB(instruction[1], instruction[2], instruction[3])
            elif name == "MULTIPLY":
                self.MUL(instruction[1], instruction[2], instruction[3])
            elif name == "DIVIDE":
                self.DIV(instruction[1], instruction[2], instruction[3])
            elif name == "INCREASE":
                self.INC(instruction[1])
            elif name == "DECREASE":
                self.DEC(instruction[1])
            elif name == "COMPARE":
                self.CMP(instruction[1], instruction[2], instruction[3], instruction[4])
            elif name == "CONST":
                self.CONST(instruction[1], instruction[2])
            elif name == "LOAD":
                self.LOAD(instruction[1], instruction[2], instruction[3])
            elif name == "STORE":
                self.STORE(instruction[1], instruction[2], instruction[3])
            elif name == "JMP":
                self.JMP(instruction[1], instruction[2])
            elif name == "JZ":
                self.JZ(instruction[1], instruction[2])
            elif name == "HALT":
                self.HALT()
                break
            else:
                raise Exception(f"Unsupported instruction: {name}")

    def ADD(self, arg1, arg2, result):
        self.registers[result] = self.registers[arg1] + self.registers[arg2]
        print(f"Result of ADD: {self.registers[result]}")

    def SUB(self, arg1, arg2, result):
        self.registers[result] = self.registers[arg1] - self.registers[arg2]
        print(f"Result of SUBSTRACT: {self.registers[result]}")

    def MUL(self, arg1, arg2, result):
        self.registers[result] = self.registers[arg1] * self.registers[arg2]
        print(f"Result of MULTIPLY: {self.registers[result]}")

    def DIV(self, arg1, arg2, result):
        self.registers[result] = self.registers[arg1] / self.registers[arg2]
        print(f"Result of DIVIDE: {self.registers[result]}")

    def INC(self, arg1):
        self.registers[arg1] += 1
        print(f"Incrementing {arg1} to {self.registers[arg1]}")

    def DEC(self, arg1):
        self.registers[arg1] -= 1
        print(f"Decrementing {arg1} to {self.registers[arg1]}")

    def CMP(self, op, arg1, arg2, result):
        print(f"Comparing {self.registers[arg1]} with {self.registers[arg2]} and saving to {result}")
        if op == "<":
            self.registers[result] = int(self.registers[arg1] < self.registers[arg2])
        elif op == ">":
            self.registers[result] = int(self.registers[arg1] > self.registers[arg2])
        elif op == "<=":
            self.registers[result] = int(self.registers[arg1] <= self.registers[arg2])
        elif op == ">=":
            self.registers[result] = int(self.registers[arg1] >= self.registers[arg2])
        elif op == "==":
            self.registers[result] = int(self.registers[arg1] == self.registers[arg2])
        elif op == "!=":
            self.registers[result] = int(self.registers[arg1] != self.registers[arg2])
        else:
            raise Exception("Unsupported operator")

    def CONST(self, value, arg1):
        self.registers[arg1] = value
        print(f"CONST {value} stored in {arg1}")

    def LOAD(self, rs, rd, offset):
        self.registers[rd] = self.memory[self.registers[rs] + offset]
        print(f"Loaded from memory to {rd}: {self.registers[rd]}")

    def STORE(self, rs, rd, offset):
        self.memory[self.registers[rs] + offset] = self.registers[rd]
        print(f"Stored {self.registers[rd]} into memory address {self.registers[rs] + offset}")

    def JMP(self, arg1, offset):
        self.registers["IP"] = self.registers[arg1] + offset
        print(f"Jumping to instruction {self.registers['IP']}")

    def JZ(self, arg1, arg2):
        if not self.registers[arg2]:
            print(f"Jumping to instruction {self.registers[arg1]} because {arg2} is 0")
            self.registers["IP"] = self.registers[arg1]
        else:
            print(f"Not jumping because {arg2} is not 0")

    def HALT(self):
        print("Program halted.")

# Create CPU instance
machine = CPU()

# Define program
code = [
    ('CONST', 10, 'Ra'),
    ('CONST', 20, 'Rb'),
    ('ADD', 'Ra', 'Rb', 'Rc'),
    ('HALT',)
]

# Run program
machine.run(code)
