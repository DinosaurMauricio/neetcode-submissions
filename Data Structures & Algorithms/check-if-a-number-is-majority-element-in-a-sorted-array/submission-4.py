class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1

        while l < r:

            mid = l + (r - l)//2
            print(mid)

            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1

        count = 0
        while l <= len(nums) - 1 and nums[l] == target:
            count+=1
            l+=1

        #print(count)

        return count > len(nums)/2
        #count = 0 
        #for i in nums:
        #    if i == target:
        #        count+=1
        #return count > len(nums) - count