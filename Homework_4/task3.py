first_list = [0, 1, 1, 2, 3, 3, 4, 4, 5, 6, 7, 8, 9, 9]
second_list = [1, 2, 2, 3, 4, 4, 5, 5, 6, 6]

def count_numbers(list1, list2):
    list_nums1 = [num1 for num1 in list1 if list1.count(num1) == 1]
    list_nums2 = [num2 for num2 in list2 if list2.count(num2) == 1]

    return len(list_nums1) + len(list_nums2)

print(count_numbers(first_list, second_list))