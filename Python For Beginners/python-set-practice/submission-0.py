from typing import List

def contains_duplicate(words: List[str]) -> bool:
    s = set()
    for w in words:
        if w in s:
            return True
        s.add(w)
    
    return False

# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))
