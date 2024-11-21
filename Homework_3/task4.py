def count_pairs(num_list):
    count = 0

    for num in num_list:
        num = str(num)
        for digit in num:
            if num.count(digit) >= 2:
                x = num.count(digit)
                count = (x * (x - 1)) // 2
        print(f"Number: {num} => Pairs: {count}")
        count = 0

    return ""

print(count_pairs([1111, 333, 22, 23, 56, 77777, 999999]))