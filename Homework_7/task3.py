def find_sum(nums, target):

    for first_num in range(len(nums)):
        for second_num in range(first_num + 1, len(nums)):
            if nums[first_num] + nums[second_num] == target:
                return [first_num, second_num]


print(find_sum([2, 11, 7, 15], 9))
print(find_sum([3, 2, 4], 6))
print(find_sum([3, 3], 6))