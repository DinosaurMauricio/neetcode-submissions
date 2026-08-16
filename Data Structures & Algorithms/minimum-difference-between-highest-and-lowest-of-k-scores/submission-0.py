class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()


        res = float('inf')
        for i in range(len(nums) - k + 1):
            arr = nums[i:k + i]
            res = min(res, arr[-1] - arr[0])


        return res