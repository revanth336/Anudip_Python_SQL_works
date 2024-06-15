# Function to find the Factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Example of calculating the factorial of a number
number = int(input())
factorial_result = factorial(number)
print("The factorial of", number, "is:", factorial_result)
