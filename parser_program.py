input_string1 = "(id+id)*id$"
input_string2 = "id*id$"
input_string3 = "(id*)$"


class Parser:
    def __init__(self, input):
        self.input = input
        self.position = 0
        self.current_char = self.input[self.position] if self.input else None
        self.stack = [("$", 0)] # Stack of tuples: (symbol,state)
        self.state = 0
        self.rules = {
            1: ('E', ['E', '+', 'T']),
            2: ('E', ['T']),
            3: ('T', ['T', '*', 'F']),
            4: ('T', ['F']),
            5: ('F', ['(', 'E', ')']),
            6: ('F', ['id'])
        }
        self.parsing_table = {
            0: {"id": "S5", "(": "S4", "E": 1, "T": 2, "F": 3},
            1: {"+": "S6", "$": "accept"},
            2: {"+": "R2", "*": "S7", ")": "R2", "$": "R2"},
            3: {"+": "R4", "*": "R4", ")": "R4", "$": "R4"},
            4: {"id": "S5", "(": "S4", "E": 8, "T": 2, "F": 3},
            5: {"+": "R6", "*": "R6", ")": "R6", "$": "R6"},
            6: {"id": "S5", "(": "S4", "T": 9, "F": 3},
            7: {"id": "S5", "(": "S4", "F": 10},
            8: {"+": "S6", ")": "S11"},
            9: {"+": "R1", "*": "S7", ")": "R1", "$": "R1"},
            10: {"+": "R3", "*": "R3", ")": "R3", "$": "R3"},
            11: {"+": "R5", "*": "R5", ")": "R5", "$": "R5"},
        }

    def advance(self): # Instead of advance, maybe consume for input string to be output?
        self.position += 1
        self.current_char = (self.input[self.position] if self.position < len(self.input) else None)

    def parse(self):
        """Parse the input string using the parsing table and rules"""
        while True:
            # State = top of stack, second item in tuple
            self.state = self.stack[-1][1]

            if self.current_char == "i":
                self.advance()
                self.current_char = "id"

            # Lookup action in parsing table given state and current input symbol
            action = self.parsing_table[self.state][self.current_char]

            # Call corresponding action function
            if action[0] == "S":
                self.shift(action[1])
            elif action[0] == "R":
                self.reduce(action[1])
            elif action == "accept":
                print("String is accepted")
                break
            else:
                print("String is not accepted")
                break

            self.advance()

    def shift(self, state):
        """Shift the current symbol and the next state to stack"""
        self.stack.append((self.current_char, state))

    def reduce(self, rule):
        """Reduce the stack by rhs of corresponding rule and replace with lhs and next state"""
        # Left hand side and right hand side to the equivalent lhs, rhs of tuple in production rule
        lhs,rhs = self.rules[rule]
        # Pop the stack for the number of symbols in the rhs of rule 
        for symbols in range(len(rhs)):
            self.stack.pop()
        # Push the lhs symbol of the rule and the goto state according to the most recent state and lhs symbol
        goto_state = self.parsing_table[self.stack[-1][1]][lhs]
        self.stack.append((lhs, goto_state))

    def output(self):
        """Print output of stack with input and action at every step"""
        pass

# Usage
parser = Parser(input_string1)
parser.parse()
parser.output()