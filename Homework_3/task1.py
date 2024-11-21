def fizz_buzz(num):
    result = ["FizzBuzz" if x % 5 == 0 and x % 3 == 0 else "Buzz" if x % 5 == 0 else "Fizz" if x % 3 == 0 else x for x in range(1, 101)]
    return result

print(fizz_buzz(100))