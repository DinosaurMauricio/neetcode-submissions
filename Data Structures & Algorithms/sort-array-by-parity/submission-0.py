class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
    
        j = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                #print("hre")
                nums[i], nums[j] = nums[j], nums[i]
                j+=1

            #print(nums, j)

        return nums