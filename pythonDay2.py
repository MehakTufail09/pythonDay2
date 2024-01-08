'''Develop a Python program to determine the greatest common divisor (GCD) of two numbers provided by the user.
The refactored code prioritizes modularity and readability by segregating the logic into distinct functions.
The `calculate_gcd` function focuses on GCD computation, `get_user_input` manages user input, and
`display_result` handles the presentation of the final result.
This approach enhances code organization, promoting maintainability and improving overall program readability.
'''


def calculateGCD(firstNum, secondNum):
    # Calculating the Greatest Common Divisor (GCD) of two numbers. using Euclidean algorithm
    while secondNum:  # this loop will continues to run until secondNum becomes 0
        firstNum, secondNum = secondNum, firstNum % secondNum  # here firstNum havinf value of secondNum and secondNum having value of firstNum1 % secondNum
    return abs(firstNum)  # here we are returning the absolute of firstNum so it is non negative


def gettingInput():
    # Get user input for two numbers.
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        return num1, num2
    except ValueError:
        print("Invalid input. Please enter valid integers.")
        return gettingInput()


def display(gcd):
    # displaying the result
    print(f"The Greatest Common Divisor (GCD) is: {gcd}")


def main():
    num1, num2 = gettingInput()
    gcd = calculateGCD(num1, num2)
    display(gcd)


main()

