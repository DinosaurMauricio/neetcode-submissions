class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        
        d = (arr[-1] - arr[0])//len(arr)
        l,r = 0, len(arr) - 1

        while l < r:
                mid = l + (r-l)//2

                if arr[mid] == arr[0] + mid * d:
                        l = mid + 1
                else:
                        r = mid

        return arr[0] + d*l