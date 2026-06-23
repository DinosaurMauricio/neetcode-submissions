class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        anchor = 0
        counter=0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[i], nums[anchor] = nums[anchor], nums[i]
                anchor += 1
                counter +=1

        return counter
            
