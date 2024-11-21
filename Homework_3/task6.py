def organize(num_list):

    for num in num_list:
        if num == 0:
            num_list.remove(num)
            num_list.append(0)
    return num_list

print(organize([0, 20, 56, 6, 0, 7, 8, 0, 9, 0]))
print(organize([0, 2, 0, 3, 4, 0, 8, 0, 3]))