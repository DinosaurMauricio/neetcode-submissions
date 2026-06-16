class Solution:
    def isPalindrome(self, s: str) -> bool:
        right = len(s) - 1
        s = s.lower()
        for left in range(len(s)//2):

            if not s[left].isalnum():
                continue
            
            while not s[right].isalnum():
                right-=1

            if s[right] != s[left]:
                return False

            right-=1

        return True


            
