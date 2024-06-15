# Function to generate Fibonacci series up to a certain number
def fibonacci_series(n):
    fib_series = []
    a, b = 0, 1
    while a < n:
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

# Get Fibonacci series between 0 and 50
fibonacci_numbers = fibonacci_series(50)
print("Fibonacci series between 0 and 50:", fibonacci_numbers)


