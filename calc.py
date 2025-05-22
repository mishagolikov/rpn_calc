# Define the RPNCalculator class for the calculator's logic
class RPNCalculator:
    def __init__(self):
        # Initialize an empty list to serve as the stack for our operands
        self.stack = []

    def evaluate(self, tokens):
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
    # Create an instance of the calculator
    calc = RPNCalculator()

    while True:
        try:
            # Read input from the user
            line = input("> ").strip()
        except EOFError:
            # Allow exit when pressing Ctrl+D (End of File)
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
