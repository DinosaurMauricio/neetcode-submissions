class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        characters_dict = {'(':')','{':'}', '[':']'}
        
        for character in s:
            

            if character in characters_dict.keys():
                stack.append(character)
            else:
                if stack and characters_dict[stack[-1]] == character:
                    stack.pop()
                else:
                    return False

        return not stack