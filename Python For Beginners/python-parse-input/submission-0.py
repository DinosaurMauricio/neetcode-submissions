from typing import List

def read_integers() -> List[int]:
    l = input()
    l = l.split(',')
    l = list(map(int, l))
    return l

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
