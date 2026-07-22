class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()
        n = len(nums)

        res = []


        
        for i in range(n):
            for j in range (i+1,n):
                right = n - 1
                left = j + 1
                while left < right:
                        temp = nums[left] + nums[right] + nums[i] + nums[j]
                        
                        if temp == target:
                            #print(left, right)
                            sol  = [nums[left], nums[right], nums[i], nums[j]]
                            sol.sort()
                            if sol not in res:
                                res.append(sol)
                        
                        if temp >  target:
                            right-=1
                        else:
                            left+=1

            
        return res