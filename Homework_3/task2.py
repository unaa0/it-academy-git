def list_gen_slice (list1, list2):
        new_list = [(letter1 + letter2) for letter1 in list1 for letter2 in list2]
        print(new_list)
        return new_list[::2]

def list_gen(list1, list2):
    new_list = [(letter1 + letter2) for letter1 in list1 for letter2 in list2]
    print(new_list)

    new_list = [x for x in new_list if x != "2a"]
    print(new_list)

    list_copy = new_list.copy()
    if "2a" not in list_copy:
        list_copy.append("2a")
    return list_copy


print(list_gen_slice(["a", "b"], ["b", "c", "d"]))
print(list_gen(["1", "2", "3", "4"], ["a"]))
