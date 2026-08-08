class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        major = nums[0]
        counter = 1

        for i in range(1,len(nums)):
            if nums[i] == major:
                counter+=1
            else:
                counter-=1
                if counter < 0:
                    major = nums[i]
                    counter = 1

        return major

