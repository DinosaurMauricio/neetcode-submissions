class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        current_color = 0
        for i in range(len(nums)):

            if current_color == nums[i]:
                continue
            if current_color not in nums[i+1:]:
                current_color+=1

            

            if current_color != nums[i]:

                left = i + 1 
                right = len(nums) - 1
                while left <= right:
                    if nums[left] == current_color:
                        nums[i], nums[left] = nums[left], nums[i]
                        break
                    elif nums[right] == current_color:
                        nums[i], nums[right] = nums[right], nums[i]
                        break
                    left+=1
                    right-=1

                
            