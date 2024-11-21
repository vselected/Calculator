# Create Function Called Calculator
def calculator():
    # Welcome user and explain how the program works
    print("Welcome to the Calculator!")
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("\n")


    while True:
        # Get user operator choice
        choice = input("Enter the number of the operation you want to perform (1/2/3/4): ")

        # Check if user operator choice is valid
        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice. Please select a valid option.")
            continue

        # Get numbers from the user
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the first number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        # Perform the chosen operation


        # Ask if the user wants to perform another calculation
        next_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
        if next_calculation != 'yes':
            print("Thank you for using the calculator! Goodbye!")
            break

# Run Calculator
calculator()