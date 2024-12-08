def multiplier(given_num):
    def wrapper(num):
        result = given_num * num
        return result
    return wrapper

print(multiplier(5)(4))
print(multiplier(6)(8))