def count_words(text):
    text = text.split()
    return f"{text} => There are {len(text)} words"

print(count_words("Word #$%,   jwsgvr !@#$%^ \n textetxtex text"))
print(count_words("Another, Sen\nte\nnce   \nwow\t cat 3456 345&&"))