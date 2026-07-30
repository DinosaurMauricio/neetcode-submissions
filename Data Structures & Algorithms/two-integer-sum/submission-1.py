class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}

        for i in range(len(nums)):

            num_j = target - nums[i] 
            
            if num_j in numbers.keys():
                return [numbers[num_j]  ,i]
   
            numbers[nums[i]] = i

        return [-1,-1]