class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]: 

        n = len(nums)
        i = 0 
        nums.sort()
        res = []

        while i  < n - 1 :

            L = i + 1
            R = n - 1
            while L < R:
                temp = nums[i] + nums[L] + nums [R]

                if temp == 0:
                    temp = [nums[i],nums[L],nums[R]]
                    if temp not in res:
                        res.append(temp)

                if nums[L] + nums[R] + nums[i]  < 0:
                    L+=1
                else:
                    R-=1
            i+=1
            

        return res
