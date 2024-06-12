def b(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return b(m - 1, 1)
    else:
        return b(m - 1, b(m, n - 1))

# Example usage
result = b(3, 2)
print("Result:", result)
