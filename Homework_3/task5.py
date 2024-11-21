def dup_elements(list1):
    duplicates = []
    for element in list1:
        if element not in duplicates:
            duplicates.append(element)
    return duplicates

print(dup_elements([1, 2, "a", 3, 1, 2, "a", 4, 5, "b"]))