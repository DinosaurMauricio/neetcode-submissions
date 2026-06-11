class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        res = {}

        for i in range(len(nums)):


            temp = target - nums[i]
            

            if temp in res.keys():
                return [res[temp], i]
            else:
                res[nums[i]] = i

        return []