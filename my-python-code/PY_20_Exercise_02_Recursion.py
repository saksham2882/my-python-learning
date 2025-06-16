# recursion 

# Recursive factorial function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


# Recursive Fibonacci function
def fib_recursive(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_recursive(n - 1) + fib_recursive(n - 2)


# Iterative Fibonacci function
def fibonacci(n):
    if n <= 0:
        return []
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib


# Get input and test functions
n = int(input("Enter a number: "))
print("Factorial:", factorial(n))
print("Fibonacci (recursive):", fib_recursive(n))
print("Fibonacci (iterative):", fibonacci(n))