"""
Compiler Data Model
AST = Abstract Syntax Tree
Representation of a program through a data structure

EXPR
STATEMENTS

int number = number_2 = 9

           =

number                =

             number_2   9


                     EXPR
             /                    \ 
            /                       \
           EXPR                     EXPR
          /     \                  /     \
        TYPE    NAME             EXPR   LITERAL
          |       |            /      \     |
        (int)   (number)     TYPE    NAME   9


Documentation: Compiler Data Model
This Python code represents a simple compiler data model for executing programs
 defined through a structure of classes.

Program Class:
Description: This class represents a program and contains a sequence of
instructions.

Attributes:
instructions: A list containing instructions to be executed.

Methods:
__init__(*expr): Initializes the program with the provided instructions.
__repr__(): Returns a string representation of the program's instructions.
exec(context={}): Executes the program by iterating over its instructions
and executing each one within the provided context.

VariableName Class:

Description: Represents a variable name in the program.

Attributes:
name: The literal name of the variable.

Methods:
__init__(literal_name): Initializes the variable name with the provided literal
name.

__repr__(): Returns a string representation of the variable name.
exec(context): Executes the variable name operation by setting its value to
None in the provided context.

BinaryOperation Class:

Description: Represents binary operations like assignment, addition, 
subtraction, multiplication, and division.

Attributes:

operation: The operation symbol (e.g., '=', '+', '-', '*', '/').
left_side: The left operand of the binary operation.
right_side: The right operand of the binary operation.

Methods:

__init__(operation, left_side, right_side): Initializes the binary operation
with the provided operation symbol and operands.

__repr__(): Returns a string representation of the binary operation.
exec(context): Executes the binary operation within the provided context. For
assignment operations, it sets the value of the left operand to the result of
evaluating the right operand. For arithmetic operations, it evaluates the
operation and returns the result.

Name Class:

Description: Represents an identifier (e.g., variable name) in the program.

Attributes:
name: The literal name of the identifier.

Methods:

__init__(literal_name): Initializes the identifier with the provided literal
name.

__repr__(): Returns a string representation of the identifier.

exec(context): Executes the identifier operation by retrieving its value from
the provided context.

Integer Class:

Description: Represents an integer value in the program.

Attributes:

value: The integer value.

Methods:

__init__(value): Initializes the integer with the provided value.

__repr__(): Returns a string representation of the integer.

exec(context): Executes the integer operation by returning its value.

Example Usage:
Two sample programs are instantiated and executed.

program1: Assigns values to variables a1 and a2, then computes the sum of their
products and assigns the result to result.
program2: Similar to program1, but the result is computed using a more complex
expression involving arithmetic operations.

"""


class Program():
    def __init__(self, *expr):
        self.instructions = expr    
    
    def __repr__(self):
        instructions_as_str = [str(i) for i in self.instructions]
        return "\n".join(instructions_as_str)
    
    def exec(self, context={}):
        for instance in self.instructions:
            instance.exec(context)
        print(context)


class VariableName(): # VARIABLE
    
    def __init__(self, literal_name):
        self.name = literal_name
    
    def __repr__(self):
        return f"var {self.name}"
    
    def exec(self, context):
        context[self.name] = None


class BinaryOperation():
    
    def __init__(self, operation, left_side, right_side):
        self.operation = operation 
        self.left_side = left_side
        self.right_side = right_side
    
    def __repr__(self):
        return f"{self.left_side} {self.operation} {self.right_side}"
    
    def exec(self, context):
        if self.operation == "=":
            context[self.left_side.name] = self.right_side.exec(context)
        else:
            left_val = self.left_side.exec(context)
            right_val = self.right_side.exec(context)
            if self.operation == "+":
                return left_val + right_val
            elif self.operation == "-":
                return left_val - right_val
            elif self.operation == "*":
                return left_val * right_val
            elif self.operation == "/":
                return left_val / right_val


class Name(): # IDENTIFIER 
    
    def __init__(self, literal_name):
        self.name = literal_name
    
    def __repr__(self):
        return self.name
    
    def exec(self, context):
        return context[self.name]


class Integer():
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value)

    def exec(self, context):
        return self.value


program1 = Program(
    BinaryOperation("=", VariableName("number1"), Integer(8)),
    BinaryOperation("=", VariableName("number2"), Integer(9)),
    BinaryOperation(
        "=",
        VariableName("result"),
        BinaryOperation("+", 
                        BinaryOperation("*", Name("number1"), Integer(8)),
                        BinaryOperation("*", Name("number2"), Integer(9)))
    )
)

print(f'Program #1: {program1}\n')


program2 = Program(
    BinaryOperation("=", VariableName("number1"), Integer(8)),
    BinaryOperation("=", VariableName("number2"), Integer(9)),
    BinaryOperation(
        "=",
        VariableName("result"),
        BinaryOperation(
            "+",
            BinaryOperation("*", Name("number1"), Name("number1")),
            BinaryOperation(
                "-",
                BinaryOperation("*", Name("number2"), Name("number2")),
                BinaryOperation("/", Name("number2"), Name("number2"))
            )
        )
    )
)

print(f'Program #2: {program2}\n')
