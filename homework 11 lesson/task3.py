def max_word():
    a = input('enter your string, please: ')
    word = a.split()
    return max(word, key=len)


print(max_word())
