def get_longer_word(word1: str, word2: str) -> str:
    w1 = len(word1)
    w2 = len(word2)

    if w1>= w2:
        return word1
    else:
        return word2



# do not modify below this line
print(get_longer_word("yellow", "orange"))
print(get_longer_word("red", "blue"))
print(get_longer_word("green", "blue"))
