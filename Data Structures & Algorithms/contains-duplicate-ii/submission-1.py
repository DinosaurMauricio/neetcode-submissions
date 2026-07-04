
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        num_dict = {}

        for i, num in enumerate(nums):

            if num in num_dict.keys():
                ind = num_dict[num] - i 
                    
                ind = ind if ind> 0 else -1*(ind)
                if ind <= k:
                    return True
                
            num_dict[num] = i

        return False
        # O(n^2)
        i, j  = 0, len(nums) - 1 

        for i in range(len(nums)):
            for j in range(i+1 ,len(nums)):
                if nums[i] == nums[j]:
                    ind = i - j if i - j > 0 else -1*(i-j)
                    if ind <= k:
                        return True
                
        return False