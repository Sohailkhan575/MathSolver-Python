def calculator():
    # Dictionary to map user choices to arithmetic operations
    operations = {
        '1': lambda x, y: x + y,  # Addition
        '2': lambda x, y: x - y,  # Subtraction
        '3': lambda x, y: x * y,  # Multiplication
        '4': lambda x, y: x / y if y != 0 else "Error! Division by zero."  # Division
    }

    while True:  # Loop to keep the calculator running
        # Display the menu
        print("\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
        choice = input("Enter choice (1/2/3/4) or 'q' to quit: ")

        if choice == 'q':  # Exit the calculator
            print("Exiting calculator. Goodbye!")
            break

        if choice in operations:  # Check if the choice is valid
            try:
                # Get input numbers from the user
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                # Perform the selected operation and display the result
                result = operations[choice](num1, num2)
                print(f"Result: {result}")
            except ValueError:  # Handle invalid input (non-numeric values)
                print("Invalid input! Please enter numbers only.")
        else:
            print("Invalid choice! Please select a valid option.")

# Run the calculator
calculator()