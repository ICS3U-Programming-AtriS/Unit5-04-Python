#!/usr/bin/env python3
# Created By: Atri Sarker
# Date: May 12, 2025
# DESCRIPTION HERE


def calculate(sign: str, num1: float, num2: float) -> float:
    # MATCH sign with operand
    match sign:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case "/":
            return num1 / num2
        case "%":
            return num1 % num2


def main():
    # Get user's operator
    user_sign = input("Enter a sign (+, -, *, /, %): ")
    # Get user's first number as a string
    num1_string = input("Enter the first number: ")
    # Get user's second number as a string
    num2_string = input("Enter the second number: ")

    # Please let me use [return 0]
    try:
        # Convert the user's input to a float
        num1 = float(num1_string)
        try:
            # Convert the user's input to a float
            num2 = float(num2_string)
            # Check if the user's sign is allowed
            if (
                user_sign == "+"
                or user_sign == "-"
                or user_sign == "*"
                or user_sign == "/"
                or user_sign == "%"
            ):
                # Prevent division by 0
                if (num2 == 0) and (user_sign == "/" or user_sign == "%"):
                    print("Division by 0 is prohibited.")
                else:
                    # CALL calculate() and get the result
                    result = calculate(user_sign, num1, num2)
                    # Display the result
                    print(f"{num1} {user_sign} {num2} = {result}")
            else:
                print(f"{user_sign} is not a recognized operator.")
        except ValueError:
            # Tell the user that their input wasn't a number
            print(f"{num2_string} is not a valid number.")
        pass
    except ValueError:
        # Tell the user that their input wasn't a number
        print(f"{num1_string} is not a valid number.")


if __name__ == "__main__":
    main()
