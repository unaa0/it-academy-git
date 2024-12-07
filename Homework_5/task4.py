def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)

print(factorial(3))
print(factorial(12))
print(factorial(1))