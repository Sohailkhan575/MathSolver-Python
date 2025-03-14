from sympy import symbols, Eq, solve

# Main Algebraic Puzzle Solver
def algebraic_puzzle_solver():
    print("Welcome to the Algebraic Puzzle Solver!")
    print("This solver can handle equations with multiple variables.")
    print("Enter your equations in the form 'x + y = 5' or '2*x - y/2 = 3'.")
    print("Type 'done' when you're finished entering equations.")

    # Collect variables and equations
    variables = set()
    equations = []

    while True:
        equation_input = input("Enter an equation (or 'done' to finish): ").strip()
        if equation_input.lower() == 'done':
            break

        try:
            # Parse the equation
            left, right = equation_input.split('=')
            left = left.strip()
            right = right.strip()

            # Extract variables
            expr = left + " - (" + right + ")"
            vars_in_expr = symbols(left + " " + right)
            variables.update(vars_in_expr)

            # Create a symbolic equation
            equation = Eq(eval(left), eval(right))
            equations.append(equation)
        except Exception as e:
            print(f"Invalid equation: {e}. Please try again.")

    if not equations:
        print("No equations provided. Exiting.")
        return

    # Solve the system of equations
    try:
        solutions = solve(equations, symbols(' '.join(map(str, variables))))
        if not solutions:
            print("No solution exists.")
        else:
            print("Solutions:")
            for var, value in solutions.items():
                print(f"{var} = {value}")
    except Exception as e:
        print(f"Error solving equations: {e}")

# Run the Algebraic Puzzle Solver
algebraic_puzzle_solver()