def factorial(num):
    if num == 1:
        return num
    else:
        return num * factorial(num - 1)

print(factorial(3))
print(factorial(12))
print(factorial(1))