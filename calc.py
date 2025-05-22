# Define the RPNCalculator class for the calculator's logic
class RPNCalculator:
    def __init__(self):
        # Initialize an empty list to serve as the stack for our operands
        self.stack = []

    def evaluate(self, tokens):
        # Process each token in the input
        for token in tokens:
            if token in ('+', '-', '*', '/'):
                # Pop the last two numbers from the stack
                b = self.stack.pop()
                a = self.stack.pop()
                
                # Use a dict to determine the result based on the operator
                result = {
                    '+': a + b,
                    '-': a - b,
                    '*': a * b,
                    '/': a / b,  # TODO: Implement div by 0 handling
                }[token]

                # Push the result back onto the stack
                self.stack.append(result)
            else:
                # If token is a number, convert to float and push onto the stack
                self.stack.append(float(token))
        
        # Print the top value of the stack (the latest result)
        print(self.stack[-1])

# Main def for running the calculator in a loop the user can communicate with
def main():
    # Create an instance of the calculator
    calc = RPNCalculator()

    while True:
        # Read input from the user
        line = input("> ").strip()

        # Quit if user enters 'q'
        if line == 'q':
            break

        # Split the input line into tokens (numbers/operators)
        tokens = line.split()

        # Evaluate the tokens using the calc
        calc.evaluate(tokens)

# Run the main loop
if __name__ == "__main__":
    main()
