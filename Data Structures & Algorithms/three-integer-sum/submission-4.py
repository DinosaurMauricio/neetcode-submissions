class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]: 

        n = len(nums)
        i = 0 
        nums.sort()
        res = []

        while i  < n - 1 :
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                i+=1
                continue

            L = i + 1
            R = n - 1
            while L < R:
                temp = nums[i] + nums[L] + nums [R]
                if temp  < 0:
                    L+=1
                elif temp > 0:
                    R-=1
                else:
                    res.append([nums[i],nums[L],nums[R]])

                    L+=1
                    R-=1

                    while L < R and  nums[L] == nums[L-1]:
                        L+=1
            i+=1
        return res
