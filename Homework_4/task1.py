def dict_gen():

    for num1 in range(1, 21):
        num2 = num1 ** 3
        new_dict = {num1 : num2}
        yield new_dict

a = dict_gen()

for number in a:
    print(number)