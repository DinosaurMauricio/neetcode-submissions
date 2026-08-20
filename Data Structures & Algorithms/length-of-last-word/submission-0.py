class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        

        
        i = 0
        s = s.split()
        return len(s[-1])
