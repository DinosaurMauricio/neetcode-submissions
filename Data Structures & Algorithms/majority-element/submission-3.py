class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        major = nums[0]
        counter = 1

        for i in range(1,len(nums)):
            if nums[i] == major:
                counter+=1
            else:
                counter-=1
                if counter < 0:
                    major = nums[i]
                    counter = 1

        return major


        # solution is o(1) space but nlogn cuz of sort
        

        if len(nums) == 1:
            return nums[0]


        nums.sort()
        major = nums[0]
        counter = 1
        p_counter = 0
        res = -1

        for i in range(1,len(nums)):

            if nums[i] == major:
                counter+=1
            else:
                major = nums[i]
                counter = 1

            if counter > p_counter:
                p_counter = counter
                major, res = nums[i],nums[i]
                    
                
        return res


        # solution is o(n) space
        dict_counter = {}
        num_major = 0
        res = -1

        for num in nums:
            dict_counter[num] = dict_counter.get(num,0) + 1


        #print(dict_counter)
        for key, value in dict_counter.items():
            if value > num_major:
                num_major = value
                res = key
        
        return res

        