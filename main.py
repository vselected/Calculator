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

    # Check if user choice is valid
    while True:
        # Get user choice
        choice = input("Enter the number of the operation you want to perform (1/2/3/4): ")

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice. Please select a valid option.")
        else:
            return choice



# Run Calculator
calculator()