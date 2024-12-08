def create_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count

    return counter

new_counter = create_counter()

print(new_counter())
print(new_counter())
print(new_counter())