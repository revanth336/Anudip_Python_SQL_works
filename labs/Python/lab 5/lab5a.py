try:
    numerator = float(input("Enter the numerator: "))
    denominator = float(input("Enter the denominator: "))
    
    result = numerator / denominator
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
