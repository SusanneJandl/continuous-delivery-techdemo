from calculator.calculator import Calculator

"""Entry point of the calculator application."""
def main():
    print("\nWelcome to the Python Calculator!")
    print("This calculator can perform the following operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("\nType 'exit' at any time to quit the calculator.\n")

    calc = Calculator()

    while True:
        try:
            # Get user input
            num1_input = input("Enter the first number: ")
            if num1_input.lower() == 'exit':
                break
            try:
                num1 = float(num1_input)
            except ValueError:
                print("Invalid input. Please enter valid numbers.\n")
                continue

            operator = input("Enter an operator (+, -, *, /): ")
            if operator.lower() == 'exit':
                break
            if not operator == '+' or not operator == '-' or not operator == '*' or not operator == '/':
                print("Invalid operator. Please enter one of +, -, *, /.\n")
                continue

            num2_input = input("Enter the second number: ")
            if num2_input.lower() == 'exit':
                break
            try:
                num2 = float(num2_input)
            except ValueError:
                print("Invalid input. Please enter valid numbers.\n")
                continue

            # Perform the calculation
            if operator == '+':
                result = calc.add(num1, num2)
            elif operator == '-':
                result = calc.subtract(num1, num2)
            elif operator == '*':
                result = calc.multiply(num1, num2)
            elif operator == '/':
                if num2 == 0:
                    print("Division by zero is not allowed.\n")
                    continue
                result = calc.divide(num1, num2)
            else:
                print("Invalid operator. Please enter one of +, -, *, /.\n")
                continue

            print(f"Result: {num1} {operator} {num2} = {result}\n")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            continue


if __name__ == "__main__":
    main()
