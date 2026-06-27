class Solution:
    def isValid(self, s: str) -> bool:
        queue = []

        for char in s:
            if char in ['{','[','(']:
                queue.append(char)
            
            else:
                if not queue:
                    return False

                if char == '}' and queue[-1] != '{' or char == ']' and queue[-1] != '[' or char == ')' and queue[-1] != '(' :
                    return False

                else:
                    queue.pop()


        return not queue