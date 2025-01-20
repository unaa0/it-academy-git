def add_one(list1):

    combined_digits = "".join([str(num) for num in list1])
    new_num = str(int(combined_digits) + 1)

    return list(new_num)

print(add_one([4, 5]))
print(add_one([1, 2, 3]))
print(add_one([9]))