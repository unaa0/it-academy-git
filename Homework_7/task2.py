def roman(roman_number):
    numeral_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    answer = 0
    current_value = 0
    next_value = 0

    for symbol in range(len(roman_number)):
        for roman_num, number in numeral_dict.items():
            if roman_number[symbol] == roman_num:
                current_value = number
                break
        if symbol < len(roman_number) - 1:
            for roman_num, number in numeral_dict.items():
                if roman_number[symbol + 1] == roman_num:
                    next_value = number
                    break
            if current_value < next_value:
                answer -= current_value
            else:
                answer += current_value
        else:
            answer += current_value

    return answer


print(roman("III"))
print(roman("LVIII"))
print(roman("MCMXCIV"))
