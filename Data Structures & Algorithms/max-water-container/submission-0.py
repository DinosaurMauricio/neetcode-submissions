class Solution:
    def maxArea(self, heights: List[int]) -> int:

        res = 0
        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                max_cap = heights[i] if heights[j] > heights[i] else heights[j]
                total = (j-i) * max_cap
                
 
                res = max(res, total)

        return res