class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        possible_start = []
        res = 0
        for n in nums:
            if n-1 not in nums:
                #possible_start.append(n)
                count = 1
                while n + 1 in nums:
                    n+=1
                    count+=1

                if res < count:
                    res = count 
        
        return res
        # but this makes it nlog n
        nums.sort()
        nums = list(set(nums))
        res, max_value = 1, 0
        nums_sort = nums[0]
        
        for i in range(1,len(nums)):
            if nums[i] == nums_sort + 1:
                print("lol")
                res+=1
            else:
                res = 0

            if res > max_value:
                max_value = res

            nums_sort = nums[i]
        return max_value
        