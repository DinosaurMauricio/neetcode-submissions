class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        res = 0
        while i < j:
            min_h = min(heights[i], heights[j])
            res = max((j-i)*min_h,res)

            if heights[i] < heights[j]:
                i+=1
            else:
                j-=1

        return res