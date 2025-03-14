import math

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Function to check if a number is composite
def is_composite(n):
    return n > 1 and not is_prime(n)

# Function to find prime factors of a number (Fundamental Theorem of Arithmetic)
def prime_factors(n):
    factors = []
    # Divide by 2 until n is odd
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    # Check for odd factors from 3 to sqrt(n)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    # If n is still greater than 2, it must be prime
    if n > 2:
        factors.append(n)
    return factors

# Function to apply the Pythagorean Theorem
def pythagorean_theorem(a, b, c=None):
    if c is None:  # Find hypotenuse
        return math.sqrt(a**2 + b**2)
    elif a is None:  # Find side a
        return math.sqrt(c**2 - b**2)
    elif b is None:  # Find side b
        return math.sqrt(c**2 - a**2)

# Main Geometry Calculator
def geometry_calculator():
    while True:
        print("\nGeometry Calculator")
        print("1. Check if a number is prime")
        print("2. Check if a number is composite")
        print("3. Find prime factors of a number (Fundamental Theorem of Arithmetic)")
        print("4. Apply the Pythagorean Theorem")
        print("5. Exit")
        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':  # Prime number check
            num = int(input("Enter a number to check if it is prime: "))
            print(f"{num} is {'prime' if is_prime(num) else 'not prime'}.")

        elif choice == '2':  # Composite number check
            num = int(input("Enter a number to check if it is composite: "))
            print(f"{num} is {'composite' if is_composite(num) else 'not composite'}.")

        elif choice == '3':  # Prime factors
            num = int(input("Enter a number to find its prime factors: "))
            factors = prime_factors(num)
            print(f"Prime factors of {num}: {factors}")

        elif choice == '4':  # Pythagorean Theorem
            print("Enter two known sides and leave the unknown side as 0.")
            a = float(input("Side a: "))
            b = float(input("Side b: "))
            c = float(input("Side c (hypotenuse): "))
            if a == 0:
                result = pythagorean_theorem(None, b, c)
                print(f"Side a = {result:.2f}")
            elif b == 0:
                result = pythagorean_theorem(a, None, c)
                print(f"Side b = {result:.2f}")
            elif c == 0:
                result = pythagorean_theorem(a, b)
                print(f"Hypotenuse c = {result:.2f}")
            else:
                print("Invalid input! At least one side must be 0.")

        elif choice == '5':  # Exit
            print("Exiting Geometry Calculator. Goodbye!")
            break

        else:
            print("Invalid choice! Please select a valid option.")

# Run the Geometry Calculator
geometry_calculator()