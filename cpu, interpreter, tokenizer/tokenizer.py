import re

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

class Tokenizer:
    def __init__(self, text):
        self.text = text
        self.pos = 0

    def tokenize(self):
        tokens = []
        while self.pos < len(self.text):
            char = self.text[self.pos]

            # Skip whitespace
            if char.isspace():
                self.pos += 1
                continue

            # Match identifiers (words)
            if re.match(r'[a-zA-Z]', char):
                identifier = self.consume_while(lambda c: c.isalnum())
                tokens.append(Token('IDENTIFIER:', identifier))

            # Match numbers
            elif re.match(r'\d', char):
                number = self.consume_while(lambda c: c.isdigit())
                tokens.append(Token('NUMBER:', number))

            # Match operators
            elif char in '+-*/=':
                tokens.append(Token('OPERATOR:', char))
                self.pos += 1

            # Match parentheses
            elif char in '()':
                tokens.append(Token('PARENTHESES:', char))
                self.pos += 1

            else:
                raise ValueError(f"Invalid character: {char}")

        return tokens

    def consume_while(self, condition):
        result = ''
        while self.pos < len(self.text) and condition(self.text[self.pos]):
            result += self.text[self.pos]
            self.pos += 1
        return result

# Example usage:
text = "x = 10 + (y * 5)"
tokenizer = Tokenizer(text)
tokens = tokenizer.tokenize()

for token in tokens:
    print(token.type, token.value)
