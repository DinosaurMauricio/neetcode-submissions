class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        values = {}

        for num in nums:
            values[num] = values.get(num, 0) + 1

            if values[num] > 1:
                return True
        return False