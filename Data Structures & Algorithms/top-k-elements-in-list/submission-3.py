class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(len(nums) + 1) ]
        temp = {}
        
        for i in range(len(nums)):
            temp[nums[i]] =  temp.get(nums[i], 0) + 1

        for key, value in temp.items():
            buckets[value].append(key)
            
        res = []
        for i  in range(len(buckets) - 1, -1, -1):
           # print(buckets[i])
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return []