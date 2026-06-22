class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)

        for i in range(n):
            right = n - 1
            left = i + 1

            while left < right:

                sum_nums = nums[left] + nums[right] + nums[i]

                if sum_nums == 0:
                    sol = [nums[left], nums[right], nums[i]]
                    
                    if sol not in res:
                        res.append(sol)
                    #left+=1

                if -(nums[left] + nums[right]) < nums[i]:
                    right-=1
                else:
                    left+=1

                

        return res
