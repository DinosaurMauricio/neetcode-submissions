class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        

        n = len(nums)
        left, right = 0, n -1

        while left < right:

            mid = left + (right - left)//2
            print(mid, left , right)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
            print(left,right)
        else:


            if target > nums[left]:
                return left + 1

            if target < nums[left] and left - 1 < 0:
                return 0
                
            return left