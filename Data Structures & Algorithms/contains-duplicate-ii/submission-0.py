
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i, j  = 0, len(nums) - 1 

        for i in range(len(nums)):
            for j in range(i+1 ,len(nums)):
                if nums[i] == nums[j]:
                    ind = i - j if i - j > 0 else -1*(i-j)
                    if ind <= k:
                        return True
                
        return False