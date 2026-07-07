class Solution:
    def maxArea(self, heights: List[int]) -> int:

        i,j = 0, len(heights) -1
        res = 0
        while i  < j:
            max_cap = min(heights[i], heights[j])
            total = (j-i) * max_cap
            res = max(total, res)

            if heights[i] >= heights[j]:
                j-=1
            else:
                i+=1

        return res

        #O(n^2) sol
        res = 0
        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                max_cap = heights[i] if heights[j] > heights[i] else heights[j]
                total = (j-i) * max_cap
                
 
                res = max(res, total)

        return res