class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        if len(nums2) < 1:
            return

        
        while m + n > 0:
            index = m + n - 1
            #print(n,m,index)
            if m > 0 and nums1[m-1] > nums2[n - 1] or n == 0:
                nums1[index] = nums1[m-1]
                m-=1
            elif n > 0:
                nums1[index] = nums2[n - 1]
                n-=1
