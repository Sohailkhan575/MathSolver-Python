import math

# Function to solve modular arithmetic (a^b mod m)
def modular_exponentiation(a, b, m):
    return pow(a, b, m)

# Function to solve linear congruence (ax ≡ b mod m)
def solve_linear_congruence(a, b, m):
    gcd_a_m = math.gcd(a, m)
    if b % gcd_a_m != 0:
        return "No solution exists."
    # Simplify the congruence
    a //= gcd_a_m
    b //= gcd_a_m
    m //= gcd_a_m
    # Find the modular inverse of a modulo m
    try:
        inverse = pow(a, -1, m)
    except ValueError:
        return "Modular inverse does not exist."
    x = (b * inverse) % m
    return f"x ≡ {x} mod {m}"

# Function to compute the continued fraction representation of a number
def continued_fraction(x, tolerance=1e-10):
    coefficients = []
    while abs(x - int(x)) > tolerance:
        coefficients.append(int(x))
        x = 1 / (x - coefficients[-1])
    coefficients.append(int(x))
    return coefficients

# Function to convert continued fraction to a rational number
def continued_fraction_to_rational(coefficients):
    numerator, denominator = 1, 0
    for coeff in reversed(coefficients):
        numerator, denominator = coeff * numerator + denominator, numerator
    return numerator, denominator

# Main Advanced Mathematics Solver
def advanced_math_solver():
    while True:
        print("\nAdvanced Mathematics Solver")
        print("1. Modular Exponentiation (a^b mod m)")
        print("2. Solve Linear Congruence (ax ≡ b mod m)")
        print("3. Continued Fraction Representation")
        print("4. Exit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':  # Modular Exponentiation
            a = int(input("Enter base (a): "))
            b = int(input("Enter exponent (b): "))
            m = int(input("Enter modulus (m): "))
            result = modular_exponentiation(a, b, m)
            print(f"{a}^{b} mod {m} = {result}")

        elif choice == '2':  # Linear Congruence
            a = int(input("Enter coefficient (a): "))
            b = int(input("Enter constant (b): "))
            m = int(input("Enter modulus (m): "))
            result = solve_linear_congruence(a, b, m)
            print(f"Solution to {a}x ≡ {b} mod {m}: {result}")

        elif choice == '3':  # Continued Fraction
            x = float(input("Enter a number to find its continued fraction representation: "))
            coefficients = continued_fraction(x)
            print(f"Continued Fraction Representation: {coefficients}")
            numerator, denominator = continued_fraction_to_rational(coefficients)
            print(f"Rational Approximation: {numerator}/{denominator} ≈ {numerator / denominator}")

        elif choice == '4':  # Exit
            print("Exiting Advanced Mathematics Solver. Goodbye!")
            break

        else:
            print("Invalid choice! Please select a valid option.")

# Run the Advanced Mathematics Solver
advanced_math_solver()