class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) -1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]

            print(right, left)
            if right - 1 <= left:
                right = len(numbers) -1
                left+=1
            else:
                right-=1
        
        return []


