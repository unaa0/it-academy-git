def list_in_list(list1):

    if not isinstance(list1, list):
        return 0

    lists_inside = 0
    for lists in list1:
        lists_nested = list_in_list(lists)
        if lists_nested > lists_inside:
            lists_inside = lists_nested

    return lists_inside + 1

print(list_in_list([[]]))
print(list_in_list([1, [2, [3]]]))
print(list_in_list([[[[]]], []]))
print(list_in_list([2]))
