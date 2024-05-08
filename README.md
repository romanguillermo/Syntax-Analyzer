# CPSC 323 Project 2 - Syntax-Analyzer
Guillermo Roman - Parser_program.py, Parse trees, and Documentation\
Gautham Vegeraju\
Julio Villegas

Parser_program.py implements a parser for a context free grammar using its production rules and parsing table. It takes an input string and parses it to determine if it is accepted by the grammar.

The program will parse the three input strings: (id+id)* id$, id* id$, and (id*)$ and display the stack, input, action table and the result.

You can edit the input strings or create a new Parser instance with a new input string

## Documentation

### Code Structure

The code defines a `Parser` class that contains the following main components:

- `__init__(self, input)`: Initializes the parser with the input string, production rules, and parsing table.
- `next_char(self)`: Removes the first character from the input and sets the current character to the next character.
- `parse(self)`: Parses the input string using the parsing table and rules to determine actions and displays the output.
- `shift(self, state)`: Shifts the current symbol and the next state to the stack.
- `reduce(self, rule)`: Reduces the stack by the right-hand side of the corresponding rule and replaces it with the left-hand side and the next state.

### Parsing Process

1. Initialize the stack with the starting symbol and state.
2. While the input string is not empty or the stack is not empty:
- Look up the action in the parsing table based on the current state and input symbol.
- If the action is "Shift":
  - Push the current symbol and the next state onto the stack.
  - Move to the next character in the input string.
- If the action is "Reduce":
  - Pop the symbols from the stack based on the right-hand side of the corresponding rule.
  - Push the left-hand side symbol and the next state onto the stack.
- If the action is "Accepted":
  - The input string is accepted by the grammar.
  - Break the loop.
- If no action is found:
  - The input string is not accepted by the grammar.
  - Break the loop.
3. Display the parsing steps and the result (accepted or not accepted).

### Results

The program outputs a table showing the parsing steps for each input string. The table includes the following columns:

- Step: The step number.
- Stack: The current state of the stack.
- Input: The remaining input string.
- Action: The action taken based on the parsing table (Shift, Reduce, or Accepted).

At the end, the program displays whether the input string is accepted or not accepted by the grammar.