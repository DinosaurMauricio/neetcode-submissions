class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict_pos = {']':'[', '}':'{', ')':'('}

        for c in s:
            if c in dict_pos:
                if stack and dict_pos[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False