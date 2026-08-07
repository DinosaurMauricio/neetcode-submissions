class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) -1

        while left < right:

            sum_values = numbers[left] + numbers[right]
            

            if sum_values > target:
                right-=1
            elif sum_values < target:
                
                left+=1
            else:
                return [left+1, right+1]

        return [0,0]

