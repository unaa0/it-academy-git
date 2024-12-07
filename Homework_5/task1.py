def gen_words(num):
    words_ascii = []

    for i in range(num):
        if num < 10:
            val = i + 65
            words_ascii.append(chr(val))
        else:
            val = i + 97 // 2
            words_ascii.append(chr(val))

    yield " ".join(words_ascii)

def in_file():
    with open("task1.txt", "w") as new_file:
        for word in gen_words(6):
            new_file.write(str(word))

        new_file.write("\n")

        for word in gen_words(15):
            new_file.write(str(word))

in_file()