def factorial(n):
    """
    Calculate the factorial of a non-negative integer n.
    
    Parameters:
    n (int): A non-negative integer whose factorial is to be computed.
    
    Returns:
    int: The factorial of the given number n.
    """
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: n * factorial of (n-1)
    return n * factorial(n - 1)

# Example usage
number = 5
result = factorial(number)
print(f"Factorial of {number} is {result}")
