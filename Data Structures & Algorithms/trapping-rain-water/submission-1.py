class Solution:
    def trap(self, height: List[int]) -> int:
        suffix_max = [0]*len(height)
        prefix_max = [0]*len(height)


        suffix_max[0] = height[0]
        for i in range(1, len(height)):
            suffix_max[i] = max(suffix_max[i-1], height[i])
            

        prefix_max[len(height) - 1] = height[len(height) -1]
        for i in range(len(height) - 2, -1, -1 ):
            prefix_max[i] = max(prefix_max[i + 1], height[i])

        max_area = 0

        for i in range(len(height)):
            a = min(suffix_max[i], prefix_max[i]) - height[i]
            if a > 0:
                max_area += a 

        return max_area
        
