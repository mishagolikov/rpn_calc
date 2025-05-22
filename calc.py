import math

# Util function to print the ASCII banner
def print_ascii():
    print(r"""
___  ____     _           _      ____________ _   _   _____       _      
|  \/  (_)   | |         ( )     | ___ \ ___ \ \ | | /  __ \     | |     
| .  . |_ ___| |__   __ _|/ ___  | |_/ / |_/ /  \| | | /  \/ __ _| | ___ 
| |\/| | / __| '_ \ / _` | / __| |    /|  __/| . ` | | |    / _` | |/ __|
| |  | | \__ \ | | | (_| | \__ \ | |\ \| |   | |\  | | \__/\ (_| | | (__ 
\_|  |_/_|___/_| |_|\__,_| |___/ \_| \_\_|   \_| \_/  \____/\__,_|_|\___|
    """)

# Define the RPNCalculator class for the calculator's logic
class RPNCalculator:
    def __init__(self):
        # Initialize an empty list to serve as the stack for our operands
        self.stack = []

    def evaluate(self, tokens):
        """
        Evaluate a list of RPN tokens.
        Supports 4 basic arithmetic operations: +, -, *, /
        """
        # Process each token in the input
        for token in tokens:
            try:
                if token in ('+', '-', '*', '/'):
                    # Make sure there are enough operands on the stack
                    if len(self.stack) < 2:
                        raise ValueError("Not enough operands on the stack")

                    # Pop the last two numbers from the stack
                    b = self.stack.pop()
                    a = self.stack.pop()

                    # Use a dict to determine the result based on the operator, handling division by 0
                    result = {
                        '+': a + b,
                        '-': a - b,
                        '*': a * b,
                        '/': a / b if b != 0 else float('inf'),
                    }[token]

                    # Push the result back onto the stack
                    self.stack.append(result)
                else:
                    # If token is a number, convert to float and push onto the stack
                    self.stack.append(float(token))

            except Exception as e:
                # Catch and print errors like bad input or simple math issues
                print(f"Error: {e}")
                return
        
        # Print the top value of the stack (the latest result)
        if self.stack:
            print(self.stack[-1])
        else:
            print(0.0)

# Main def for running the calculator in a loop the user can communicate with
def main():
    """
    Launch the RPN calculator loop on command line for user to interact with.
    Accepts user input until 'q' or 'Ctrl+D' is entered (or 'Ctrl+Z' on Windows).
    """
    # Intro message for user
    print_ascii()
    print("Welcome to Misha's RPN Calculator.")
    print("Enter numbers and operators (+ - * /), one per line or space-separated.")
    print("Type 'q' to quit. Press Ctrl+D (Unix) or Ctrl+Z then Enter (Windows) to exit.")

    # Create an instance of the calculator
    calc = RPNCalculator()

    while True:
        try:
            # Read input from the user
            line = input("> ").strip()
        except EOFError:
            # Allow exit when pressing Ctrl+D (or Ctrl+Z then Enter on Windows)
            print("\nExiting on EOF.")
            break

        # Quit if user enters 'q'
        if line == 'q':
            break

        # Skip empty lines
        if not line:
            continue

        # Split the input line into tokens (numbers/operators)
        tokens = line.split()

        # Evaluate the tokens using the calc
        calc.evaluate(tokens)

# Run the main loop
if __name__ == "__main__":
    main()
