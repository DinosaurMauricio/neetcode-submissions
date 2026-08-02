class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 0
        vals = set()
        res = 0

        while i < len(s):
            
            #print(vals)
            if s[i] not in vals:
                vals.add(s[i])
                i+=1
            else:
                vals.remove(s[j])
                j+=1
                

            res = max(res, len(vals))
        
        return res