class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res_dict = {num: 0 for num in set(nums)}
        res = []
        
        for num in nums:
            res_dict[num]+=1


        sorted_ele = sorted(res_dict.items(), key= lambda x: x[1], reverse=True)

        for i in range(k):
            res.append(sorted_ele[i][0])

        return res