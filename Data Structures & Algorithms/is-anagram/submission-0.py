class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_string = {}
        for c in s:
            s_string[c] = s_string.get(c,0) + 1

        for c in t:
            s_string[c] = s_string.get(c,0) - 1

        for c in s_string.values():
            if c<0 or c != 0:
                return False
        return True
    
