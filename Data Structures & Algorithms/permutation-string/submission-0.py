class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s2) < len(s1):
            return False

        s1_freq = [0]*26
        s2_freq = [0]*26

        for c in s1:
            s1_freq[ ord(c) - ord('a')] += 1


        left = 0
        right = len(s1)-1

        while right < len(s2):
            #print(left, right)
            for i in range(left, right + 1):
                s2_freq[ ord(s2[i]) - ord('a')] += 1

            if s2_freq == s1_freq:
                return True

            s2_freq = [0]*26
            left += 1
            right+=1

        return False