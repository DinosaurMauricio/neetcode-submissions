class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0 ,0
        res = 0
        storage = set()

        while j < len(s):

            if s[j] not in storage:
                storage.add(s[j])
                j+=1
            else:
                storage.remove(s[i])
                i +=1
                
            res = max(res, j - i)


        return res
        
