input_string1 = "(id+id)*id$"
input_string2 = "id*id$"
input_string3 = "(id*)$"


class Parser:
    def __init__(self, input):
        self.input_const = input  # For output
        self.input = input
        self.current_char = self.input[0] if self.input else None
        self.stack = [("$", 0)]  # Stack of tuples: (symbol,state)
        self.state = 0
        self.rules = (
            {  # production rules: lhs = first item of tuple, rhs = second item of tuple
                1: ("E", ["E", "+", "T"]),
                2: ("E", ["T"]),
                3: ("T", ["T", "*", "F"]),
                4: ("T", ["F"]),
                5: ("F", ["(", "E", ")"]),
                6: ("F", ["id"]),
            }
        )
        self.parsing_table = {
            0: {"id": "S5", "(": "S4", "E": 1, "T": 2, "F": 3},
            1: {"+": "S6", "$": "Accepted"},
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

    def next_char(self):
        """Removes first character from input and sets current char to next character (first of updated input)"""
        self.input = self.input[1:]
        self.current_char = self.input[0] if self.input else None

    def parse(self):
        """Parse the input string using the parsing table and rules and display output"""
        steps = []  # For tracking the steps of the parser for output table
        step = 0
        while True:
            step += 1
            # State = second item in (symbol,state) tuple at top of stack
            self.state = int(self.stack[-1][1])

            if (
                self.current_char == "i"
            ):  # If current symbol is 'i', assume symbol is 'id'
                self.current_char = "id"

            # Lookup action in parsing table given state and current input symbol
            if (
                self.current_char in self.parsing_table[self.state]
            ):  # If action exists for current state and symbol
                action = self.parsing_table[self.state][self.current_char]
                steps.append(
                    (step, self.stack.copy(), self.input, action)
                )  # Append step to steps list before action is taken
                if action[0] == "S":
                    state = int(action[1:])
                    self.shift(state)
                    if self.current_char == "id":  # if 'id', skip two characters
                        self.next_char()
                        self.next_char()
                    else:
                        self.next_char()
                elif action[0] == "R":
                    rule = int(action[1:])
                    self.reduce(rule)
                elif action == "Accepted":
                    self.accepted = True
                    break
            else:  # If no valid action for current state and symbol, accepted is false, add last valid step to stack output before breaking
                steps.append((step, self.stack.copy(), self.input, action))
                self.accepted = False
                break

        # Output table
        print(f"Input: {self.input_const}")
        print("Stack:")
        print(f"{'Step':<5}\t{'Stack':<25}\t{'Input':<20}\t{'Action':<4}")
        print("-" * 80)
        for step, stack, input, action in steps:
            print(
                f"{step:<5}\t{' '.join([f'{s[0]} {s[1]}' for s in stack]):<25}\t{input:20}\t{action:4}"
            )

        if self.accepted:
            print("Output: String is accepted\n")
        else:
            print("Output: String is not accepted\n")

    def shift(self, state):
        """Shift the current symbol and the next state to stack"""
        self.stack.append((self.current_char, state))

    def reduce(self, rule):
        """Reduce the stack by rhs of corresponding rule and replace with lhs and next state"""
        # Left hand side and right hand side to the equivalent lhs, rhs of tuple in production rule
        lhs, rhs = self.rules[rule]
        # Pop the stack the number of symbols in the rhs of rule
        for symbols in range(len(rhs)):
            self.stack.pop()
        # Push the lhs symbol of the rule and the goto state according to the most recent state and lhs symbol
        goto_state = self.parsing_table[self.stack[-1][1]][lhs]
        self.stack.append((lhs, goto_state))


# Usage
example = Parser(input_string1)
example.parse()

example2 = Parser(input_string2)
example2.parse()

example3 = Parser(input_string3)
example3.parse()
