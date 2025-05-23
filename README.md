# RPN Calculator (Command-Line Interface)

This is a simple Reverse Polish Notation (RPN) calculator implemented in Python. It supports the four basic arithmetic operations: addition, subtraction, multiplication, and division. The calculator is designed to be run interactively in a terminal and maintains operand stack in memory during usage.

---

## High-Level Description

The RPN Calculator operates via the command line, accepting input tokens in Reverse Polish Notation. Instead of requiring parentheses or operator precedence, users enter operands followed by operators (e.g., `3 9 +`) in a single line. Users can also enter operands and operators on seperate lines after adding them to the stack. The calculator evaluates input line by line and prints the result at the top of the stack.

---

## Technical Choices & Reasoning

- **Language:** Python 3 — for its clean syntax and easy development of command line tools.
- **Architecture:** 
  - `RPNCalculator` class encapsulates all stack operations and eval logic.
  - A separate `main()` loop handles user I/O, making the program easy to test and extend.
- **Design Considerations:**
  - Input is tokenized using `split()`, enabling both single token and multi token input.
  - Proper handling of errors (e.g., invalid input, stack underflow, division by zero).
  - Cross-platform EOF support considerations for users (`Ctrl+D` on Unix, `Ctrl+Z` on Windows).
  - Added ASCII logo in intro text, just taking some creative liberty.

---

## Trade-offs & Future Improvements

### Trade-offs:
- The calculator is intentionally minimal and does not support advanced math functions, variables, or command history to maintain simplicity and clarity.
- Division by zero currently returns `inf`, instead of raising an exception. I chose to return "inf" when dividing by zero to keep the calculator from crashing or halting unexpectedly. This makes the user experience smoother and more forgiving.

### Future Improvements:
- Support additional operators like modulus, exponentiation, and square root.
- Extend I/O options (e.g., file input, WebSocket integration).
- Add command history or session save/restore.
- Wrap as a `.exe` or `.app` for easier usage on Windows/macOS/Linux.

---

## How to Run

1. Make sure you have Python 3 installed:
   ```bash
   python --version
   ```

2. Clone or download this repo, then run:
   ```bash
   python calc.py
   ```
   OR
   ```bash
   python3 calc.py
   ```
   Depending on system and Python version

3. Example usage:
   ```
   > 5
   5.0
   > 8
   8.0
   > +
   13.0
   > q
   ```
4. Run unit tests:
   ```bash
   python test_calc.py
   ```
   OR
   ```bash
   python3 test_calc.py
   ```
   Depending on system and Python version
### Special Keys:
- `q` to quit
- `Ctrl+D` (Unix/macOS) or `Ctrl+Z` + `Enter` (Windows) to send EOF and exit

---

## 📁 Project Structure

```
rpn_calc/
├── calc.py         # Main calculator script
├── test_calc.py    # Unit tests (optional extension)
└── README.md       # This file
```

---

## Author

Created by Misha Golikov
