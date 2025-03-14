import math
import numpy as np

# Function to solve a linear equation (ax + b = 0)
def solve_linear(a, b):
    if a == 0:
        return "No solution (a cannot be zero)."
    return -b / a

# Function to solve a quadratic equation (ax^2 + bx + c = 0)
def solve_quadratic(a, b, c):
    if a == 0:
        return solve_linear(b, c)  # Fallback to linear equation
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "No real solutions (discriminant < 0)."
    elif discriminant == 0:
        x = -b / (2*a)
        return f"One real solution: x = {x}"
    else:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return f"Two real solutions: x1 = {x1}, x2 = {x2}"

# Function to solve a system of linear equations (Ax = B)
def solve_system_of_equations(coefficients, constants):
    try:
        A = np.array(coefficients)
        B = np.array(constants)
        solution = np.linalg.solve(A, B)
        return f"Solution: {solution}"
    except np.linalg.LinAlgError:
        return "No unique solution (system may be inconsistent or dependent)."

# Main Algebraic Equation Solver
def algebraic_equation_solver():
    while True:
        print("\nAlgebraic Equation Solver")
        print("1. Solve Linear Equation (ax + b = 0)")
        print("2. Solve Quadratic Equation (ax^2 + bx + c = 0)")
        print("3. Solve System of Linear Equations")
        print("4. Exit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':  # Linear Equation
            a = float(input("Enter coefficient a: "))
            b = float(input("Enter coefficient b: "))
            result = solve_linear(a, b)
            print(f"Solution: {result}")

        elif choice == '2':  # Quadratic Equation
            a = float(input("Enter coefficient a: "))
            b = float(input("Enter coefficient b: "))
            c = float(input("Enter coefficient c: "))
            result = solve_quadratic(a, b, c)
            print(f"Solution: {result}")

        elif choice == '3':  # System of Linear Equations
            n = int(input("Enter the number of variables/equations: "))
            coefficients = []
            constants = []
            print("Enter the coefficients for each equation:")
            for i in range(n):
                equation_coeffs = list(map(float, input(f"Equation {i+1} coefficients (space-separated): ").split()))
                coefficients.append(equation_coeffs)
                constant = float(input(f"Enter the constant for equation {i+1}: "))
                constants.append(constant)
            result = solve_system_of_equations(coefficients, constants)
            print(result)

        elif choice == '4':  # Exit
            print("Exiting Algebraic Equation Solver. Goodbye!")
            break

        else:
            print("Invalid choice! Please select a valid option.")

# Run the Algebraic Equation Solver
algebraic_equation_solver()