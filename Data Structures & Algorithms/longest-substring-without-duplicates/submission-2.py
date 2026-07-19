class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0 ,0
        res = 0
        storage = []

        while j < len(s):

            if s[j] not in storage:
                storage.append(s[j])
                j+=1
            else:
                storage.pop(0)
                i +=1
                


            res = max(res, j - i)


        return res
        
