class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        n = set()
        
        for i in range(len(nums)):

            if nums[i] in n:
                return nums[i]

            n.add(nums[i])
