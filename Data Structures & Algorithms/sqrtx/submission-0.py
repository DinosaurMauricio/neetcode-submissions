class Solution:
    def mySqrt(self, x: int) -> int:
        L , R = 0, x


        while L <= R:
            mid = L + (R - L)//2
            if mid*mid <= x and x < (mid+1)*(mid+1):
                return mid
            if  mid*mid > x:
                R = mid - 1
            else:
                L = mid + 1 

        return -1

