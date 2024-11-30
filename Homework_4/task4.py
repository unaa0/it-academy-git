first_list = [0, 1, 2, 3, 4, 7, 9]
second_list = [1, 2, 3, 5, 6]

def count_numbers(list1, list2):
    list_nums1 = [num1 for num1 in list1 if num1 not in list2]
    list_nums2 = [num2 for num2 in list2 if num2 not in list1]

    return len(list_nums1) + len(list_nums2)

print(count_numbers(first_list, second_list))