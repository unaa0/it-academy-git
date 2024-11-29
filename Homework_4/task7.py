def euclidean(num1, num2):

    while num2 != 0:
        if num1 > num2:
            result = num1 % num2
            num1 = num2
            num2 = result

    return f"Наибольший общий делитель: {num1}"


print(euclidean(175, 90))
print(euclidean(120,  50))
print(euclidean(15, 3))