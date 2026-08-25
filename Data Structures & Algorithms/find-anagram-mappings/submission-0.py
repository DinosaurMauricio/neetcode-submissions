class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        data = {}
        res = []
        for i in range(len(nums2)):
            if nums2[i] not in data:
                data[nums2[i]] = i
        
        for n in nums1:
            res.append(data[n])

        return res