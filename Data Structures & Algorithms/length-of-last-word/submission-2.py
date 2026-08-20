class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        i = len(s) - 1

        while s[i] == ' ':
            i-=1

        counter = 0 
        while i >= 0 and s[i] != ' ':
            i-=1
            counter+=1

        return counter