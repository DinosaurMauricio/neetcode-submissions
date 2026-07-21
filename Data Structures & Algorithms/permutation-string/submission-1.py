class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s2) < len(s1):
            return False

        s1_freq = [0]*26
        s2_freq = [0]*26

        for c in s1:
            s1_freq[ ord(c) - ord('a')] += 1

        left, right = 0, 0
        
        while right < len(s2):
            
            s2_freq[ ord(s2[right]) - ord('a')] += 1
            
            if right > len(s1) - 1:
                s2_freq[ ord(s2[left]) - ord('a')] -= 1
                left+=1

            if s2_freq == s1_freq:
                return True

            right+=1

        return False