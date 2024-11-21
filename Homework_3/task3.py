def conversion(list1, tuple1):
    new_list = tuple(list1)
    new_tuple = list(tuple1)
    return new_list, new_tuple

print(conversion(["a", "b", "c"], ("a", "b", "c")))

a, b, c = "a", 2, "python"
print(f"a = {a}, b = {b}, c = {c}")

def iter_tuple(tuple1):
    sep_elements = []
    for var in tuple1:
        for letter in var:
            sep_elements.append(letter)
    print(sep_elements)
    return len(tuple1)

print(iter_tuple(("123",)))