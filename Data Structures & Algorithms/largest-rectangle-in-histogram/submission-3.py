class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0


        for i in range(len(heights) + 1):

            while stack and (len(heights) == i or heights[stack[-1]] >= heights[i]):
                

                h = heights[stack.pop()]
                width = i if not stack else (i- stack[-1]) - 1
                res = max (res, h * width)
            stack.append(i)

        return res