class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        res = 0
        count = 0

        for num in nums:
            if num == 0:
                res = max(res, count)
                count = 0
            else:
                count+=1
        
        return max(res, count)