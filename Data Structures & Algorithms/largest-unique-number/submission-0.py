class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        nums.sort()
        res = -1
        for i in range(len(nums) - 1, -1,-1):
            if nums[i] == res:
                res = -1

            elif nums[i] > res:
                res = nums[i]
            #print(res)


        return res