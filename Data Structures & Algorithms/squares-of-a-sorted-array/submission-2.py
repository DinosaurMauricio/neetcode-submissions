class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        i, j , k = 0,len(nums) -1, len(nums) - 1

        while i <= j:
            if abs(nums[j]) > abs(nums[i]):
                res[k] = nums[j]*nums[j]
                j-=1
            else:
                res[k] = nums[i]*nums[i]
                i+=1

            k-=1
        return res